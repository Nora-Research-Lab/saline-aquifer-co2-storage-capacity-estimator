![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Saline Aquifer CO2 Storage Capacity Estimator
 
*For CCS geoscientists and engineers: enter reservoir dimensions and properties to instantly estimate the theoretical CO2 storage capacity of a deep saline aquifer.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Carbon Capture & Storage (CCS)
 
**Inputs (5 fields):**  
1. **Area (A)** – numeric input, km² (e.g., 100).  
2. **Net Thickness (h)** – numeric input, meters (e.g., 50).  
3. **Porosity (φ)** – slider or numeric input, fraction 0.0–0.5 (default 0.15).  
4. **CO2 Density at reservoir conditions (ρ)** – numeric input, kg/m³ (typical range 600–900, default 700).  
5. **Storage Efficiency Factor (E)** – slider or numeric input, dimensionless 0.01–0.10 (typical 0.02–0.04, default 0.04).  

**Core calculation (step by step):**  
1. Convert area from km² to m²: A_m² = A * 1e6.  
2. Compute pore volume: V_pore = A_m² * h * φ (m³).  
3. Compute mass of CO2 that can be stored: M = V_pore * ρ * E (kg).  
4. Convert to million tonnes: M_Mt = M / 1e9.  
5. Categorize storage potential:  
   - < 10 Mt: 'Small'  
   - 10–100 Mt: 'Medium'  
   - > 100 Mt: 'Large'  

**Gradio UI layout:**  
- Title and brief instructions at top.  
- Two columns: left column has all inputs (gr.Number for area, thickness, density; gr.Slider for porosity and efficiency).  
- Right column shows a 'Calculate' button and output area: a large numeric display of estimated capacity in Mt, plus a text label with the capacity category (Small/Medium/Large) in a colored box.  
- Below outputs, a short note explaining the input ranges and that this is a screening-level estimation.  

**Output:**  
- Numerical value: 'Estimated CO2 storage capacity: X.XX Mt'  
- Classification: 'Storage potential: Large ( > 100 Mt )' with color coding (green for Large, yellow Medium, red Small).  
- No charts – clean and focused.  

**AI/ML component:** None. Pure deterministic calculation.
 
## Run it
 
```bash
docker build -t saline-aquifer-co2-storage-capacity-estimator .
docker run -p 7860:7860 saline-aquifer-co2-storage-capacity-estimator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-24.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
