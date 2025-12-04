"""
EJ RHAI Platform Backend
Flask application serving index.html and providing mock APIs for recruitment and HR analytics.

Dependencies: Flask
Installation: pip install Flask
Running: python app.py
Server will run on http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# ============================================================================
# MOCK DATA - Profiles Database
# ============================================================================

PROFILES = [
    {
        "id": 1,
        "name": "Ana Silva",
        "age": 28,
        "area": "Desenvolvimento",
        "specializations": ["Python", "JavaScript", "React"],
        "school": "USP",
        "city": "São Paulo",
        "bio": "Desenvolvedora full-stack com 5 anos de experiência em startups.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=ana",
        "available": True,
        "score_hard": 8.5,
        "score_soft": 7.8
    },
    {
        "id": 2,
        "name": "Carlos Oliveira",
        "age": 32,
        "area": "Gestão de Projetos",
        "specializations": ["Agile", "Scrum", "Kanban"],
        "school": "UFRJ",
        "city": "Rio de Janeiro",
        "bio": "Gerente de projetos experiente em transformação digital.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=carlos",
        "available": True,
        "score_hard": 8.0,
        "score_soft": 8.9
    },
    {
        "id": 3,
        "name": "Marina Costa",
        "age": 26,
        "area": "Design",
        "specializations": ["UI/UX", "Figma", "Prototipagem"],
        "school": "FAAP",
        "city": "São Paulo",
        "bio": "Designer UX/UI criativa com foco em experiência do usuário.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=marina",
        "available": True,
        "score_hard": 8.2,
        "score_soft": 8.5
    },
    {
        "id": 4,
        "name": "Ricardo Ferreira",
        "age": 35,
        "area": "Dados",
        "specializations": ["SQL", "Python", "Machine Learning"],
        "school": "UNICAMP",
        "city": "Campinas",
        "bio": "Analista de dados com expertise em machine learning e big data.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=ricardo",
        "available": True,
        "score_hard": 9.0,
        "score_soft": 7.5
    },
    {
        "id": 5,
        "name": "Juliana Martins",
        "age": 29,
        "area": "Marketing",
        "specializations": ["Marketing Digital", "SEO", "Analytics"],
        "school": "FGV",
        "city": "São Paulo",
        "bio": "Especialista em marketing digital e growth hacking.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=juliana",
        "available": True,
        "score_hard": 7.8,
        "score_soft": 8.7
    },
    {
        "id": 6,
        "name": "Felipe Gomes",
        "age": 31,
        "area": "Desenvolvimento",
        "specializations": ["Java", "Spring Boot", "Microserviços"],
        "school": "PUC-RJ",
        "city": "Rio de Janeiro",
        "bio": "Desenvolvedor backend especializado em arquiteturas escaláveis.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=felipe",
        "available": False,
        "score_hard": 8.8,
        "score_soft": 7.9
    },
    {
        "id": 7,
        "name": "Beatriz Rocha",
        "age": 27,
        "area": "Vendas",
        "specializations": ["B2B", "Negociação", "CRM"],
        "school": "INSPER",
        "city": "São Paulo",
        "bio": "Executiva de vendas com histórico de crescimento de receita.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=beatriz",
        "available": True,
        "score_hard": 7.5,
        "score_soft": 9.0
    },
    {
        "id": 8,
        "name": "Lucas Alves",
        "age": 24,
        "area": "Desenvolvimento",
        "specializations": ["TypeScript", "Node.js", "React"],
        "school": "UFMG",
        "city": "Belo Horizonte",
        "bio": "Desenvolvedor junior talentoso com sólida base em tecnologias modernas.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=lucas",
        "available": True,
        "score_hard": 7.6,
        "score_soft": 8.0
    },
    {
        "id": 9,
        "name": "Gabriela Pereira",
        "age": 33,
        "area": "Recursos Humanos",
        "specializations": ["Recrutamento", "Desenvolvimento Organizacional", "Compliance"],
        "school": "UNESP",
        "city": "São Paulo",
        "bio": "Profissional de RH com experiência em transformação cultural.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=gabriela",
        "available": True,
        "score_hard": 7.9,
        "score_soft": 8.8
    },
    {
        "id": 10,
        "name": "Thiago Santos",
        "age": 30,
        "area": "Infraestrutura",
        "specializations": ["DevOps", "AWS", "Docker", "Kubernetes"],
        "school": "UFBA",
        "city": "Salvador",
        "bio": "Especialista em infraestrutura cloud e DevOps.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=thiago",
        "available": True,
        "score_hard": 8.7,
        "score_soft": 7.6
    },
    {
        "id": 11,
        "name": "Camila Souza",
        "age": 26,
        "area": "Atendimento ao Cliente",
        "specializations": ["Suporte Técnico", "Comunicação", "Resolução de Conflitos"],
        "school": "SENAC",
        "city": "Brasília",
        "bio": "Profissional dedicada ao atendimento com excelente comunicação.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=camila",
        "available": True,
        "score_hard": 7.2,
        "score_soft": 8.9
    },
    {
        "id": 12,
        "name": "Bruno Costa",
        "age": 34,
        "area": "Finanças",
        "specializations": ["Contabilidade", "Análise Financeira", "Planejamento"],
        "school": "FEA-USP",
        "city": "São Paulo",
        "bio": "Analista financeiro com experiência em empresas multinacionais.",
        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=bruno",
        "available": True,
        "score_hard": 8.6,
        "score_soft": 7.7
    }
]

# Mock database for hiring records
HIRING_RECORDS = []

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the index.html file"""
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    """
    GET /api/profiles
    Returns list of all profiles (minimum 12 profiles)
    """
    return jsonify(PROFILES)

@app.route('/api/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    """
    GET /api/profile/<id>
    Returns detailed profile information
    """
    profile = next((p for p in PROFILES if p['id'] == profile_id), None)
    if profile:
        return jsonify(profile)
    return jsonify({"error": "Profile not found"}), 404

@app.route('/api/search', methods=['POST'])
def search_profiles():
    """
    POST /api/search
    Body: { age_min, age_max, area, specializations, school, city, q }
    Returns filtered profiles
    """
    data = request.get_json() or {}
    results = PROFILES.copy()
    
    # Filter by age range
    if 'age_min' in data:
        results = [p for p in results if p['age'] >= data['age_min']]
    if 'age_max' in data:
        results = [p for p in results if p['age'] <= data['age_max']]
    
    # Filter by area
    if data.get('area'):
        results = [p for p in results if p['area'].lower() == data['area'].lower()]
    
    # Filter by specializations (any match)
    if data.get('specializations'):
        spec_list = data['specializations'] if isinstance(data['specializations'], list) else [data['specializations']]
        results = [p for p in results if any(s.lower() in [sp.lower() for sp in p['specializations']] for s in spec_list)]
    
    # Filter by school
    if data.get('school'):
        results = [p for p in results if p['school'].lower() == data['school'].lower()]
    
    # Filter by city
    if data.get('city'):
        results = [p for p in results if p['city'].lower() == data['city'].lower()]
    
    # Filter by query string (search in name, bio, area, specializations)
    if data.get('q'):
        query = data['q'].lower()
        results = [p for p in results if 
                   query in p['name'].lower() or 
                   query in p['bio'].lower() or 
                   query in p['area'].lower() or
                   any(query in s.lower() for s in p['specializations'])]
    
    return jsonify(results)

@app.route('/api/hire', methods=['POST'])
def hire_profile():
    """
    POST /api/hire
    Body: { profile_id, company_name }
    Records a hiring action (in-memory)
    """
    data = request.get_json() or {}
    profile_id = data.get('profile_id')
    company_name = data.get('company_name', 'Unknown Company')
    
    profile = next((p for p in PROFILES if p['id'] == profile_id), None)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    hiring_record = {
        "id": len(HIRING_RECORDS) + 1,
        "profile_id": profile_id,
        "profile_name": profile['name'],
        "company_name": company_name,
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    }
    HIRING_RECORDS.append(hiring_record)
    
    return jsonify({
        "success": True,
        "message": f"{profile['name']} foi contratado(a) por {company_name}!",
        "record": hiring_record
    })

@app.route('/api/ejrhai/recommend', methods=['POST'])
def ejrhai_recommend():
    """
    POST /api/ejrhai/recommend
    Body: { role_description, filters }
    Returns 5 recommended profiles (mock)
    """
    data = request.get_json() or {}
    role_description = data.get('role_description', '')
    filters = data.get('filters', {})
    
    # Simple mock recommendation: return top 5 available profiles
    # In a real system, this would use ML/scoring
    recommended = [p for p in PROFILES if p['available']][:5]
    
    return jsonify({
        "role_description": role_description,
        "recommendations": recommended,
        "count": len(recommended)
    })

@app.route('/api/ejrhai/calc', methods=['POST'])
def ejrhai_calc():
    """
    POST /api/ejrhai/calc
    Body: { expression or request }
    Returns calculated result (mock)
    """
    data = request.get_json() or {}
    request_type = data.get('type', 'average')
    
    if request_type == 'average_hard':
        avg = sum(p['score_hard'] for p in PROFILES) / len(PROFILES)
        return jsonify({
            "type": "average_hard",
            "result": round(avg, 2),
            "label": "Média de Hard Skills"
        })
    elif request_type == 'average_soft':
        avg = sum(p['score_soft'] for p in PROFILES) / len(PROFILES)
        return jsonify({
            "type": "average_soft",
            "result": round(avg, 2),
            "label": "Média de Soft Skills"
        })
    else:
        return jsonify({
            "type": "custom",
            "result": 7.8,
            "label": "Resultado Simulado"
        })

@app.route('/api/ejrhai/analytics', methods=['GET'])
def ejrhai_analytics():
    """
    GET /api/ejrhai/analytics
    Returns analytics data for employee performance (6 months mock)
    """
    analytics = {
        "period": "6 months",
        "total_employees": len(PROFILES),
        "performance_by_area": {
            "Desenvolvimento": {
                "hard_skills": 8.3,
                "soft_skills": 7.9,
                "count": 3
            },
            "Gestão de Projetos": {
                "hard_skills": 8.0,
                "soft_skills": 8.9,
                "count": 1
            },
            "Design": {
                "hard_skills": 8.2,
                "soft_skills": 8.5,
                "count": 1
            },
            "Dados": {
                "hard_skills": 9.0,
                "soft_skills": 7.5,
                "count": 1
            },
            "Marketing": {
                "hard_skills": 7.8,
                "soft_skills": 8.7,
                "count": 1
            },
            "Vendas": {
                "hard_skills": 7.5,
                "soft_skills": 9.0,
                "count": 1
            },
            "Recursos Humanos": {
                "hard_skills": 7.9,
                "soft_skills": 8.8,
                "count": 1
            },
            "Infraestrutura": {
                "hard_skills": 8.7,
                "soft_skills": 7.6,
                "count": 1
            },
            "Atendimento ao Cliente": {
                "hard_skills": 7.2,
                "soft_skills": 8.9,
                "count": 1
            },
            "Finanças": {
                "hard_skills": 8.6,
                "soft_skills": 7.7,
                "count": 1
            }
        },
        "hiring_records": len(HIRING_RECORDS)
    }
    return jsonify(analytics)

# ============================================================================
# ERROR HANDLING
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("EJ RHAI Platform - Backend Server")
    print("=" * 70)
    print("\nStarting Flask server...")
    print("Server running on http://127.0.0.1:5000")
    print("\nTo install dependencies: pip install Flask")
    print("To run: python app.py")
    print("\nAvailable endpoints:")
    print("  GET  /api/profiles")
    print("  GET  /api/profile/<id>")
    print("  POST /api/search")
    print("  POST /api/hire")
    print("  POST /api/ejrhai/recommend")
    print("  POST /api/ejrhai/calc")
    print("  GET  /api/ejrhai/analytics")
    print("\n" + "=" * 70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
