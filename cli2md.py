import csv
import re
from collections import defaultdict

# === Templates ===
summary_template = """
# Awesome Command Line (CLI/TUI) Programs [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This repository - to the best of my knowledge - contains the largest collection of command line (CLI/TUI) tools available in the form of awesome list.
With source information maintained in a handy CSV file.

To contribute, see the [contribution section](#contribute).
Read the instructions before rushing at changing the README file: you must edit the CSV files, not the README!

Some links are available to [related resources](#related-resources).

## Summary:

* Apps/tools: **{n_apps}**
* Categories: **{n_cats}**

## Contents

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
## <a name=\"related-resources\"></a>Related resources

A list of some online resources that contribute interesting links to apps and info.

{resources}
"""

contribute_template = """
## <a name=\"contribute\"></a>Contribute

Found an awesome CLI/TUI tool that’s not listed here? Want to improve descriptions or fix broken links?

Please read the CONTRIBUTING guidelines in the repository before submitting a pull request.
"""

def github_anchor(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return '-' + text

def get_icon_flags(app):
    flags = []
    ai = app.get("AI", "").strip().lower()
    online = app.get("Online", "").strip().lower()
    tui_cli = app.get("TUI/CLI", "").strip().lower()

    if ai == "yes":
        flags.append("\U0001F916 ✅")
    elif ai == "no":
        flags.append("\U0001F916 ❌")

    if online == "yes":
        flags.append("\U0001F310 ✅")
    elif online == "no":
        flags.append("\U0001F310 ❌")

    if "cli" in tui_cli and "tui" in tui_cli:
        flags.append("\U0001F5A5CLI/\U0001F5A5TUI")
    elif "cli" in tui_cli:
        flags.append("\U0001F5A5CLI")
    elif "tui" in tui_cli:
        flags.append("\U0001F5A5TUI")

    return " ".join(flags)

def fmt_app(app):
    descr = app['description'].replace('\n', ' ').strip()
    name = app['name']
    link = app['homepage'] if app['homepage'].startswith('http') else app['git']
    icons = get_icon_flags(app)
    return f"* [{name}]({link}) [{icons}] - {descr}" if link else f"* {name} [{icons}] - {descr}"

def fmt_resource(res):
    return f"[{res['title']}]({res['url']}) - {res['description']}"

def fmt_toc(categories):
    toc_lines = []
    for cat in categories:
        toc_lines.append(f"### {cat['category_label']}")
        for sub in cat['subcategories']:
            anchor = github_anchor(sub['subcategory_label'])
            toc_lines.append(f"- [{sub['subcategory_label'].replace('-', ' ').title()}](#{anchor}): {sub['subcategory_description']}")
        toc_lines.append("")
    return '\n'.join(toc_lines)

def load_csv(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def generate_readme(apps_path, categories_path, resources_path, output_path):
    apps = load_csv(apps_path)
    categories = load_csv(categories_path)
    resources = load_csv(resources_path)

    seen = set()
    unique_apps = []
    for app in apps:
        key = (app['name'].strip().lower(), app['git'].strip().lower(), app['homepage'].strip().lower())
        if key not in seen:
            seen.add(key)
            unique_apps.append(app)

    grouped = defaultdict(lambda: {'category_label': '', 'subcategories': []})
    for row in categories:
        cat = row['category']
        grouped[cat]['category_label'] = row['category_label']
        grouped[cat]['subcategories'].append({
            'subcategory_name': row['subcategory'],
            'subcategory_label': row['subcategory_label'],
            'subcategory_description': row['description']
        })

    toc = fmt_toc(grouped.values())
    content_lines = []
    for cat_data in grouped.values():
        sub_lines = []
        for sub in cat_data['subcategories']:
            apps_in_sub = [a for a in unique_apps if a['Category'] == cat_data['category_label'] and a['Subcategory'] == sub['subcategory_name']]
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

    resource_lines = [fmt_resource(r) for r in resources]

    full_readme = summary_template.format(n_apps=len(unique_apps), n_cats=len(grouped), toc=toc)
    full_readme += '\n'.join(content_lines)
    full_readme += contribute_template
    full_readme += resources_template.format(resources='\n\n'.join(resource_lines))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_readme)

if __name__ == "__main__":
    generate_readme("apps.csv", "subcategories_file2.csv", "resources.csv", "README.md")
