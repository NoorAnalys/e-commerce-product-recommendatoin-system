# 📌 Pull Request Title
<!-- Example: Add product interaction tracking for AI recommendations -->

---

## 📝 Description
<!-- 
Briefly describe what this PR does.
Focus on *what* and *why*, not implementation details.
-->

---

## 🎯 Scope of Changes
<!-- Check all that apply -->

- [ ] Backend API (FastAPI)
- [ ] Database / Models
- [ ] Schemas (Pydantic)
- [ ] Services / Business Logic
- [ ] Authentication / Security
- [ ] AI Recommendation (Notebooks)
- [ ] AI Recommendation (ML Service)
- [ ] Configuration / Environment
- [ ] Docker / Deployment
- [ ] Documentation (README / Docs)
- [ ] Tests

---

## 🔧 Key Changes
<!-- List main changes clearly -->

- 
- 
- 

---

## 🤖 AI Impact (if applicable)
<!-- Fill this section only if AI/recommendation is affected -->

- Interaction data affected:  
  - [ ] Views
  - [ ] Likes
  - [ ] Favorites
  - [ ] Orders
- Model / feature changes:
- Impact on recommendation results:

---

## 🗂️ Files / Modules Affected
<!-- Example paths -->

- `app/api/routes/...`
- `app/models/...`
- `app/services/...`
- `ml_notebooks/...`
- `ml_service/...`

---

## 🧪 How to Test
<!-- Provide clear steps -->

1. Run backend:
   ```bash
   uvicorn app.main:app --reload
Test endpoint:

bash
Copy code
curl http://localhost:8000/...
(Optional) Run ML service:

bash
Copy code
uvicorn app.main:app --reload --port 9000
✅ Checklist
<!-- Must be checked before merging -->
 Code follows project structure

 No breaking API changes (or documented)

 Environment variables documented

 Database migrations included (if needed)

 AI service compatibility checked (if applicable)

 Tests added / updated

 README updated (if needed)

🚀 Deployment Notes (Optional)
<!-- Any special steps needed after merge -->
📎 Related Issues / Tasks
<!-- Example: Closes #12 -->
Closes #
