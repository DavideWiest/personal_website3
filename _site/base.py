from django.utils import translation
import json
import datetime

std_title_clause = " - Davide Wiest"
lang_independant_files = ("credentials", "data")
allowed_languages = ("en", "de")


def openfile(filename, subfield=None, base_path=None):
    if base_path == None:
        base_path = "_site"
    with open(f"{base_path}/static/_content/{filename}", "r", encoding="utf-8") as f:
        file = json.load(f)
        if subfield:
            file = file.get(subfield, file)

    return file

def build_params(title, storage_ptrs, params, language, base_path=None):
    
    c_files = {}
    for storage_ptr in storage_ptrs + ["base"]:
        if storage_ptr != "":
            if "/" in storage_ptr:
                filename, subfield = storage_ptr.split("/")
            else:
                filename, subfield = (storage_ptr, "")
            
            c_files[filename + "_" + subfield.capitalize() if subfield != "" else filename] = openfile(language + "_" + filename + ".json" if filename not in lang_independant_files else filename + ".json", subfield=subfield if subfield != "" else None, base_path=base_path)
        else:
            c_files[filename] = {}

    alternative_langs = list(allowed_languages)
    alternative_langs.remove(language)
    
    dt = datetime.date.today()

    bparams = {
        "title": title + std_title_clause,
        "base_url": "https://davidewiest.com",
        "year": dt.strftime("%Y"),
        "c": c_files,
        "l": language,
        "other_langs": alternative_langs
    }

    return {**bparams, **params}

def choose_lang(request):
    language = translation.get_language_from_request(request)

    # first priority
    if request.method == "GET":
        if request.GET.get("language") in allowed_languages:
            # change request.session["language"]
            # change db user settings.language
            return request.GET.get("language")
    
    # second priority
    if "user_id" in request.session:
        # change request.session["language"] with db
        pass
    
    # third priority
    if request.session.get("language") in allowed_languages:
        return request.session["language"]
    
    # allow only de or en
    if language in ("ch", "au"):
        language = "de"
    if language != "de":
        language = "en"

    # testing !!!
    language = "en"

    return language

def handle_requestdata(request, l):
    if request.GET.get("language") in allowed_languages:
        request.session["language"] = l
        return request.GET.get("language")
        
    if request.session.get("language") not in allowed_languages:
        request.session["language"] = l

    