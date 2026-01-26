"""
Scrape Vena API Recipes from developers.venasolutions.com/recipes
Tries multiple methods: requests-html (if available), or manual inspection
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
import time
import json

def scrape_with_requests_html():
    """Try using requests-html for JavaScript rendering."""
    try:
        from requests_html import HTMLSession
        print("Using requests-html to render JavaScript...")
        session = HTMLSession()
        r = session.get("https://developers.venasolutions.com/recipes", timeout=30)
        print("Rendering JavaScript (this may take a moment)...")
        r.html.render(timeout=30, wait=5, sleep=2)  # Render JavaScript with longer wait
        print("JavaScript rendered successfully!")
        return r.html.html
    except ImportError as e:
        print(f"requests-html not available: {e}")
        return None
    except Exception as e:
        print(f"requests-html failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def scrape_vena_recipes():
    """Scrape recipes from Vena API Recipes page."""
    
    url = "https://developers.venasolutions.com/recipes"
    
    print(f"Fetching recipes from: {url}")
    
    # Try requests-html first
    html_content = scrape_with_requests_html()
    
    if not html_content:
        print("Trying standard requests (may miss JavaScript-rendered content)...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        html_content = response.text
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try to extract JSON data from script tags
    recipes_data = []
    script_tags = soup.find_all('script', type='application/json')
    for script in script_tags:
        try:
            data = json.loads(script.string)
            # Look for recipe data in the JSON
            if isinstance(data, dict):
                # Check for recipes in various possible locations
                if 'recipes' in str(data).lower() or 'tutorial' in str(data).lower():
                    recipes_data.append(data)
        except:
            pass
    
    # Find recipe links
    recipe_links = []
    all_links = soup.find_all('a', href=re.compile(r'/recipes/'))
    
    for link in all_links:
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href and text:
            if href.startswith('/'):
                href = f"https://developers.venasolutions.com{href}"
            # Avoid duplicates
            if href not in [r['href'] for r in recipe_links]:
                recipe_links.append({'href': href, 'text': text})
    
    # Extract main content
    main_content = soup.find('main')
    content_text = ""
    if main_content:
        content_text = main_content.get_text(separator='\n', strip=True)
    
    # Save output
    output_dir = Path(__file__).parent.parent / "knowledge_base" / "Modeler" / "Data Transformation & Integration"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Build markdown content
    markdown_content = f"""# Vena API Recipes

**Source:** {url}
**Scraped:** {time.strftime('%Y-%m-%d %H:%M:%S')}
**Total Recipes Found:** {len(recipe_links)}

## Recipes

"""
    
    if recipe_links:
        for i, recipe in enumerate(recipe_links, 1):
            markdown_content += f"{i}. [{recipe['text']}]({recipe['href']})\n"
    else:
        markdown_content += "No recipe links found. The page may require JavaScript rendering.\n"
        markdown_content += "\n**Note:** To get all recipes, you may need to:\n"
        markdown_content += "1. Install requests-html: `pip install requests-html`\n"
        markdown_content += "2. Or use Selenium with ChromeDriver\n"
        markdown_content += "3. Or manually visit the page and copy the recipe list\n"
    
    if content_text:
        markdown_content += f"\n## Page Content Preview\n\n{content_text[:3000]}"
    
    # Save markdown
    md_file = output_dir / "(Reference) - Vena API Recipes - Scraped.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"\nSaved markdown to: {md_file}")
    print(f"Found {len(recipe_links)} recipe links")
    
    return md_file, len(recipe_links)


if __name__ == "__main__":
    result = scrape_vena_recipes()
    if result:
        print(f"\nSuccessfully scraped recipes to: {result}")
    else:
        print("\nFailed to scrape recipes")
