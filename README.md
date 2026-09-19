![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Drill Core Recovery & RQD Calculator
 
*For mining geologists and engineers: enter core run, recovered length, and intact piece totals to instantly get core recovery, RQD, and rock-quality classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Mining & Minerals
 
This tool computes core recovery and Rock Quality Designation (RQD) from a single diamond drill run. The user provides three positive numeric inputs in meters: (a) total drilled core run length, (b) total length of core recovered, and (c) summed length of sound, intact core pieces equal to or longer than 0.10 m. The tool validates that recovered length is not greater than the total run length and that the summed intact-piece length is not greater than recovered length. Core recovery percentage is calculated as recovered length divided by total run length, multiplied by 100. RQD percentage is calculated as the summed length of intact pieces equal to or longer than 0.10 m divided by total run length, multiplied by 100. RQD is classified using the standard Deere classification: 0–25% very poor, 25–50% poor, 50–75% fair, 75–90% good, and 90–100% excellent. Core recovery is also interpreted with practical bands: less than 75% poor, 75–90% fair, 90–95% good, and 95–100% excellent. The Gradio interface uses three numeric input boxes labeled 'Core Run Length (m)', 'Recovered Core Length (m)', and 'Sum of Intact Pieces ≥ 0.10 m (m)', a 'Calculate' button, and a results panel. Outputs include the two percentages rounded to one decimal place, the RQD classification, the core recovery classification, and a simple horizontal RQD gauge image showing the value from 0 to 100 against colored quality bands. No AI/ML component is needed; this is a deterministic domain calculation.
 
## Run it
 
```bash
docker build -t drill-core-recovery-rqd-calculator .
docker run -p 7860:7860 drill-core-recovery-rqd-calculator
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
 
Built 2026-09-19.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
