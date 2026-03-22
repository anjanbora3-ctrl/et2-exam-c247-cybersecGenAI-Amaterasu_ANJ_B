# Attack Surface Monitoring and Security Audit System

## 🚀 Overview
This system provides continuous, automated security auditing for cloud infrastructure (Terraform) and application dependencies. It is designed to identify security risks early in the development lifecycle by analyzing configurations for public exposure, insecure network settings, and vulnerable third-party libraries.

## 🛡️ Key Features
- **Infrastructure Security Monitoring:** Analyzes Terraform `.tf` files to detect publicly exposed servers, insecure storage, and open management ports (SSH/RDP).
- **Dependency Scanning:** Scans application manifests (`package.json`) to identify high-risk and critical vulnerabilities in third-party packages.
- **Automated CI/CD Audits:** Integrated with GitHub Actions to perform security checks on every code push or pull request.
- **Actionable Reporting:** Generates detailed JSON and text-based audit summaries for rapid remediation.

## 📁 Project Structure
- `infrastructure/`: Contains Terraform configuration files generated from the security dataset.
- `app/`: Contains the application's dependency manifest (`package.json`).
- `scripts/`:
  - `audit.py`: The core auditing engine that performs infrastructure and dependency analysis.
  - `setup_project.py`: Utility script used to initialize the project from the source dataset.
- `docs/`: Contains the comprehensive `FINAL_REPORT.md` with detailed findings and recommendations.
- `.github/workflows/`: Contains the `security_audit.yml` CI/CD pipeline configuration.

## ⚙️ How It Works
1.  **Detection:** The `audit.py` script parses infrastructure files and dependency lists.
2.  **Analysis:** It matches configurations against security best practices (e.g., checking for `public_access = true` or open port `22`).
3.  **Reporting:** Results are aggregated into a summary report, categorizing the overall security posture (e.g., CRITICAL or WARNING).
4.  **Automation:** GitHub Actions executes this process automatically, ensuring that no insecure configuration is deployed without an audit.

## 📊 Latest Audit Summary
- **Total Risks Identified:** 264
- **Exposed Services:** 99
- **High-Risk Dependencies:** 100
- **Security Posture:** **CRITICAL**

## 🛠️ Requirements
- Python 3.11+
- `pandas`
- `openpyxl`

## 📝 License
This project is developed as part of a Scenario-Based Assessment for Attack Surface Monitoring and Security Auditing.
