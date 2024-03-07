// wwwroot/scripts/custom.js

window.clearTokenFromUrl = function (removeText) {
    // Convert removeText to a string
    removeText = removeText.toString();

    // Create a regular expression to match the token in the URL
    var regex = new RegExp('/' + removeText, 'g');

    // Get the current URL
    var currentUrl = window.location.href;

    // Clear the token from the URL
    var newUrl = currentUrl.replace(regex, '');

    // Replace the URL without the token
    history.replaceState({}, document.title, newUrl);
}

window.copyToClipboard1 = {
    writeText: function (text) {
        // Create a textarea element to hold the text
        var textarea = document.createElement("textarea");
        textarea.value = text;

        // Append the textarea to the document
        document.body.appendChild(textarea);

        // Select and copy the text
        textarea.select();
        document.execCommand("copy");

        // Remove the textarea from the document
        document.body.removeChild(textarea);
    }
};

window.showDeleteIcon = function (elementName, projects) {
    var currentProj = document.getElementById("projectName_" + elementName);
    var delIcon = document.getElementById("deleteProj_" + elementName);
    if (currentProj) {
        if (currentProj.style.display == 'flex') {
            delIcon.style.display = 'block';
        }
    }
}

window.hideDeleteIcon = function (elementName) {
    var currentProj = document.getElementById("projectName_" + elementName);
    var delIcon = document.getElementById("deleteProj_" + elementName);
    if (currentProj) {
        delIcon.style.display = 'none';
        //if (currentProj.style.display == 'flex') {
        //    delIcon.style.display = 'none';
        //}
    }
}

window.cancelDelete = function (elementName) {
    var confirmDeleteEle = document.getElementById("confirmDelete_" + elementName);
    var currentProj = document.getElementById("projectName_" + elementName);
    if (currentProj) {
        currentProj.style.display = 'flex';
        confirmDeleteEle.style.visibility = 'hidden';
        confirmDeleteEle.style.left = '-100%';
        confirmDeleteEle.style.position = 'absolute';
    }
}

window.showElementById = function (elementName, projects) {
    for (var item in projects) {
        var confirmDeleteEle = document.getElementById("confirmDelete_" + projects[item]);
        var currentProj = document.getElementById("projectName_" + projects[item])
        var delIcon = document.getElementById("deleteProj_" + projects[item]);
        if (projects[item] == elementName) {
            if (currentProj) {
                currentProj.style.display = 'none';
            }
            if (confirmDeleteEle) {
                confirmDeleteEle.style.visibility = 'visible';
                confirmDeleteEle.style.left = '-10px';
                confirmDeleteEle.style.position = 'relative';
            }
        } else {
            if (currentProj) {
                currentProj.style.display = 'flex';
            }
            if (confirmDeleteEle) {
                confirmDeleteEle.style.visibility = 'hidden';
                confirmDeleteEle.style.left = '-100%';
                confirmDeleteEle.style.position = 'absolute';
            }
        }
    }

    //var confirmDeleteEle = document.getElementById("confirmDelete_" + elementName);
    //var currentProj = document.getElementById("projectName_" + elementName)
    //if(currentProj)
    //{
    //    currentProj.style.display = 'none';
    //}
    //if (confirmDeleteEle) {
    //    confirmDeleteEle.style.left = '0';
    //    confirmDeleteEle.style.position = 'relative';
    //}
}

window.hideConfirmDelAlrt = function (parentID) {
    document.addEventListener('click', function (event) {
        var currentele = event.target;
        var isClosest = currentele.closest(parentID);
        if (isClosest == null) {
            var parent = document.getElementById(parentID);
            parent.querySelectorAll("div[id^='confirmDelete_']").forEach(function (div) {
                div.style.visibility = 'hidden';
                div.style.left = '-100%';
                div.style.position = 'absolute';
            });
            parent.querySelectorAll("div[id^='projectName_']").forEach(function (div) {
                div.style.display = 'flex';
            });
        }
    });
}