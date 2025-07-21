import csv
import string
from collections import defaultdict

# === Templates ===
summary_template = """
Summary:

* Apps/tools: **{n_apps}**
* Categories: **{n_cats}**

# Contents

{toc}
"""

subcategory_section_template = """
## 📁 {subcategory_label}
{subcategory_description}

{apps}
"""

category_section_template = """
# {category_label}

{subcategories}
"""

resources_template = """
# <a name="resources"></a>Related resources

A list of some online resources that contribute interesting links to apps and info.

{resources}
"""

# === Loaders ===
def load_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as infile:
        return list(csv.DictReader(infile))

# === Formatters ===
def fmt_app(app):
    descr = app['description'].replace('\n', ' ').strip()
    name = app['name']
    link = app['homepage'] if app['homepage'].startswith('http') else app['git']
    if not link:
        return f"* {name} - {descr}"
    return f"* [{name}]({link}) - {descr}"

def fmt_resource(res):
    return f"[{res['title']}]({res['url']}) - {res['description']}"

def github_anchor(text):
    import re
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return '-' + text

def fmt_toc(categories):
    toc_lines = []
    for cat in categories:
        toc_lines.append(f"### {cat['category_label']}")
        for sub in cat['subcategories']:
            anchor = github_anchor(sub['subcategory_label'])
            toc_lines.append(f"- [{sub['subcategory_label'].replace('-', ' ').title()}](#{anchor}): {sub['subcategory_description']}")
        toc_lines.append("")
    return '\n'.join(toc_lines)

# === Main Markdown Generator ===
def generate_readme(apps, cleaned_categories, resources):
    # Organize subcategories under categories
    grouped = defaultdict(lambda: {'category_label': '', 'subcategories': []})
    for row in cleaned_categories:
        cat = row['category_name']
        grouped[cat]['category_label'] = row['category_label']
        grouped[cat]['subcategories'].append({
            'subcategory_name': row['subcategory_name'],
            'subcategory_label': row['subcategory_label'],
            'subcategory_description': row['subcategory_description']
        })

    # Prepare TOC
    toc = fmt_toc(grouped.values())

    # Prepare content sections
    content_lines = []
    for cat_data in grouped.values():
        sub_lines = []
        for sub in cat_data['subcategories']:
            apps_in_sub = [a for a in apps if a['Category'] == cat_data['category_label'] and a['Subcategory'] == sub['subcategory_name']]
            if not apps_in_sub:
                continue
            app_lines = [fmt_app(app) for app in sorted(apps_in_sub, key=lambda x: x['name'].lower())]
            sub_block = subcategory_section_template.format(
                subcategory_label=sub['subcategory_label'],
                subcategory_description=sub['subcategory_description'],
                apps='\n'.join(app_lines)
            )
            sub_lines.append(sub_block)

        if sub_lines:
            content_lines.append(category_section_template.format(
                category_label=cat_data['category_label'],
                subcategories='\n'.join(sub_lines)
            ))

    # Prepare resources section
    resources_section = ""
    if resources:
        resource_lines = [fmt_resource(r) for r in resources]
        resources_section = resources_template.format(resources='\n\n'.join(resource_lines))

    # Combine all sections
    summary = summary_template.format(n_apps=len(apps), n_cats=len(grouped), toc=toc)
    return summary + '\n\n' + '\n'.join(content_lines) + '\n\n' + resources_section

# === Example Usage ===
# apps = load_csv('apps.csv')
# cleaned_categories = load_csv('compact_categories_subcategories_cleaned.csv')
# resources = load_csv('resources.csv')
# markdown = generate_readme(apps, cleaned_categories, resources)
# print(markdown)
