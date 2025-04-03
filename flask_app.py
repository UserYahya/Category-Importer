from flask import Flask, request, render_template
import pywikibot

app = Flask(__name__)

# Set user agent to avoid throttling
pywikibot.config.user_agent = "CategoryImporterBot/1.0 (by User:Yahya)"


def get_en_cats(page_title):
    site_bn = pywikibot.Site('bn', 'wikipedia')
    bn_page = pywikibot.Page(site_bn, page_title.strip())

    if not bn_page.exists():
        return [], "The page does not exist on Bangla Wikipedia."

    site_en = pywikibot.Site('en', 'wikipedia')
    enwiki_key = site_en.dbName()  # 'enwiki'

    try:
        item = pywikibot.ItemPage.fromPage(bn_page)
        item.get()

        if enwiki_key in item.sitelinks:
            en_title = item.sitelinks[enwiki_key].title
            en_page = pywikibot.Page(site_en, en_title)
            return [cat for cat in en_page.categories() if not cat.isHiddenCategory()], None
        else:
            return [], "No English Wikipedia article linked to this page."
    except pywikibot.exceptions.NoPageError:
        return [], "No Wikidata item found for this Bangla page."
    except Exception as e:
        return [], f"Unexpected error: {str(e)}"


def get_bn_cats(en_cats):
    site_bn = pywikibot.Site('bn', 'wikipedia')
    bnwiki_key = site_bn.dbName()  # 'bnwiki'
    bn_cats = []

    for en_cat in en_cats:
        try:
            item = en_cat.data_item()
            item.get()

            if bnwiki_key in item.sitelinks:
                bn_title = item.sitelinks[bnwiki_key].title
                bn_cat = pywikibot.Page(site_bn, bn_title)
                bn_cats.append(bn_cat)
        except Exception:
            continue

    return bn_cats


@app.route('/', methods=['GET', 'POST'])
def index():
    categories_markup = ""
    error_message = ""

    if request.method == 'POST':
        page_title = request.form['page_title'].strip()
        en_cats, error = get_en_cats(page_title)
        if error:
            error_message = error
        else:
            bn_cats = get_bn_cats(en_cats)
            if bn_cats:
                categories_markup = "\n".join(
                    f"[[বিষয়শ্রেণী:{cat.title(with_ns=False)}]]" for cat in bn_cats
                )
            else:
                error_message = "No equivalent Bangla categories found."

    return render_template('index.html', categories_markup=categories_markup, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
