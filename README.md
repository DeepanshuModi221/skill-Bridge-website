# skill-Bridge-website
3rd sem project
# Skill Bridge (demo)

This is a small static demo site named "Skill Bridge" where users can search and access courses and check job listings.

Files created:
- `index.html` — main single-page UI (no backend)
- `styles.css` — basic styling
- `app.js` — client-side logic to load and filter `courses.json` and `jobs.json`
- `data/courses.json` — sample course entries
- `data/jobs.json` — sample job entries

How to run locally (two options):

Option A — Python built-in HTTP server (recommended)

Open PowerShell in this folder and run:

```powershell
# serve on port 8000
cd 'C:\Users\dell\OneDrive\Desktop\DeepanshuP\skill-bridge'; python -m http.server 8000; `
# then open http://localhost:8000 in your browser
```

Option B — VS Code Live Server extension

Install Live Server, open this folder in VS Code and click "Go Live".

Notes and next steps:
- This is a static demo using local JSON. For production, connect to an API or database.
- You can expand features: pagination, login, enrollments, saved jobs, filters by skill level.
- If you want, I can convert this into a React app or add a small Node/Express API.

Enjoy — tell me if you want more features or a different stack!
