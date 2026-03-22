import pandas as pd
import os

# Create directories
os.makedirs('infrastructure', exist_ok=True)
os.makedirs('app', exist_ok=True)
os.makedirs('scripts', exist_ok=True)
os.makedirs('.github/workflows', exist_ok=True)
os.makedirs('reports', exist_ok=True)
os.makedirs('docs', exist_ok=True)

# Load dataset
df = pd.read_excel('ET2-DATASET-MAIN.xlsx')

# Generate Terraform files
for index, row in df.iterrows():
    tf_filename = f"infrastructure/{row['Infrastructure_File']}"
    with open(tf_filename, 'w') as f:
        f.write(f'resource "aws_{row["Resource_Type"].lower()}" "example_{index}" {{\n')
        f.write(f'  name = "{row["Infrastructure_File"]}"\n')
        f.write(f'  port = {row["Port_Configuration"]}\n')
        f.write(f'  public_access = {"true" if row["Public_Access"] == "Yes" else "false"}\n')
        f.write('}\n')

# Generate package.json
dependencies = df[['Application_Dependency', 'Dependency_Version']].drop_duplicates()
with open('app/package.json', 'w') as f:
    f.write('{\n  "name": "security-audit-app",\n  "version": "1.0.0",\n  "dependencies": {\n')
    dep_lines = [f'    "{row["Application_Dependency"]}": "{row["Dependency_Version"]}"' for _, row in dependencies.iterrows()]
    f.write(',\n'.join(dep_lines))
    f.write('\n  }\n}\n')

print("Project files generated successfully.")
