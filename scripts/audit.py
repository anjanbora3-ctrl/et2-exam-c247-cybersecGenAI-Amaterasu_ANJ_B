import os
import json
import pandas as pd

def audit_infrastructure():
    results = []
    df = pd.read_excel('ET2-DATASET-MAIN.xlsx')
    
    infra_dir = 'infrastructure'
    for filename in os.listdir(infra_dir):
        if filename.endswith('.tf'):
            filepath = os.path.join(infra_dir, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                
                # Extract details from file (simulated parsing)
                is_public = 'public_access = true' in content
                
                # Find the row in the dataframe corresponding to this file
                row = df[df['Infrastructure_File'] == filename].iloc[0]
                
                if is_public:
                    results.append({
                        'type': 'Infrastructure',
                        'file': filename,
                        'resource': row['Resource_Type'],
                        'risk': 'Publicly Exposed Server',
                        'severity': 'High' if row['Resource_Type'] in ['EC2', 'VM'] else 'Medium'
                    })
                
                if row['Port_Configuration'] in [22, 80, 443, 3389]:
                    results.append({
                        'type': 'Infrastructure',
                        'file': filename,
                        'resource': row['Resource_Type'],
                        'risk': f"Open Network Port: {row['Port_Configuration']}",
                        'severity': 'High'
                    })
    return results

def audit_dependencies():
    results = []
    df = pd.read_excel('ET2-DATASET-MAIN.xlsx')
    
    # Unique vulnerabilities from dataset
    vulnerabilities = df[['Application_Dependency', 'Dependency_Version', 'Vulnerability_Severity']].drop_duplicates()
    
    for _, row in vulnerabilities.iterrows():
        if row['Vulnerability_Severity'] in ['High', 'Critical']:
            results.append({
                'type': 'Dependency',
                'name': row['Application_Dependency'],
                'version': row['Dependency_Version'],
                'risk': f"Vulnerable Dependency ({row['Vulnerability_Severity']})",
                'severity': row['Vulnerability_Severity']
            })
    return results

def generate_report(infra_results, dep_results):
    os.makedirs('reports', exist_ok=True)
    report = {
        'summary': {
            'exposed_services': len([r for r in infra_results if r['risk'] == 'Publicly Exposed Server']),
            'high_risk_dependencies': len([r for r in dep_results if r['severity'] in ['High', 'Critical']]),
            'insecure_infrastructure_configs': len(infra_results),
            'total_risks': len(infra_results) + len(dep_results)
        },
        'details': {
            'infrastructure': infra_results,
            'dependencies': dep_results
        }
    }
    
    with open('reports/audit_report.json', 'w') as f:
        json.dump(report, f, indent=4)
        
    with open('reports/audit_summary.txt', 'w') as f:
        f.write("ATTACK SURFACE MONITORING - SECURITY AUDIT SUMMARY\n")
        f.write("==================================================\n\n")
        f.write(f"Total Risks Found: {report['summary']['total_risks']}\n")
        f.write(f"Exposed Services: {report['summary']['exposed_services']}\n")
        f.write(f"High-Risk Dependencies: {report['summary']['high_risk_dependencies']}\n")
        f.write(f"Insecure Infrastructure Configs: {report['summary']['insecure_infrastructure_configs']}\n")
        f.write("\nSECURITY POSTURE: " + ("CRITICAL" if report['summary']['total_risks'] > 50 else "WARNING") + "\n")
        
    print(f"Audit completed. Report saved to reports/audit_report.json and reports/audit_summary.txt")

if __name__ == "__main__":
    infra_results = audit_infrastructure()
    dep_results = audit_dependencies()
    generate_report(infra_results, dep_results)
