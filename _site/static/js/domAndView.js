document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelectorAll('img').forEach(function(img){
        img.onerror = function(){this.style.visibility='hidden';};
    })
});

document.addEventListener("DOMContentLoaded", function(event) {
    if (localStorage.getItem('fromPage').split("?")[0] == String(window.location.href).split("?")[0]) {
        var scrollpos = localStorage.getItem('scrollpos');
        if (scrollpos) window.scrollTo(0, scrollpos);
    }
});


function toggleNavMobile(elem) {
    const div = document.querySelector('#navbar-links');
    if (div != null) {
        if (div.classList.contains("hidden")) {
            div.classList.remove("hidden");
        } else {
            div.classList.add("hidden");
            if (document.activeElement == elem) {
                elem.blur();
            }
        }
    }
}

window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
    localStorage.setItem('fromPage', window.location.href);
};

document.addEventListener('click', function handleClickOutsideBox(event) {
    const div = document.getElementById('navbar-links');
    const btn = document.getElementById('toggle-nav-mobile-btn');
    
    if (div != null) {
        if (!div.contains(event.target) && !btn.contains(event.target)) {
            div.classList.add("hidden");
        }
    }
});

document.getElementById('toggle-nav-mobile-btn').addEventListener('focusout', (event) => {
    const div = document.getElementById('navbar-links');
    if (div != null) {
        if (event.relatedTarget == div) {
            const btn = document.getElementById('toggle-nav-mobile-btn');
            btn.focus();
        }
    }
});

function revealLangOptions() {
    const div = document.querySelector('#language-options-inner');
    if (div != null) {
        if (div.classList.contains("hidden")) {
            div.classList.remove("hidden");
        } else {
            div.classList.add("hidden");
        }
    }
}

document.addEventListener('click', function handleClickOutsideBox(event) {
    const div = document.getElementById('language-options-inner');
    const btn = document.getElementById('show-languages');
    
    if (div != null) {
        if (!div.contains(event.target) && !btn.contains(event.target)) {
            div.classList.add("hidden");
        }
    }
});

function sizeNav() {
    if (document.getElementById("special-announcement") != null && screen.width < 767) {
        var top1 = document.getElementById("special-announcement").offsetHeight;
        document.getElementById("navbar-links").style.top = String(62 + top1) + "px";
    } else if (screen.width >= 767) {
        document.getElementById("navbar-links").style.top = String(0) + "px";
    }
}

window.addEventListener("resize", sizeNav)

sizeNav();

try {
    document.querySelector("div.CookieDeclaration").classList.add("text-sm", "px-4");
} catch (error) {
    
}
