// fuction to add new work experience field
function addNewWField(){
    let newNode = document.createElement("textarea");
    newNode.classList.add("workexp");
    newNode.setAttribute("name", "workexp");
    newNode.setAttribute("rows", 3);
    newNode.setAttribute("cols", 30);
    newNode.setAttribute("placeholder", "Enter your work experience here...");
    
    // variable for the container inside which the field will be dynamically placed
    let we = document.getElementById("we");

    // variable for the element before which the new field is to be placed
    let weAddButton = document.getElementById("weAddBtn");

    we.insertBefore(newNode, weAddButton);
}

// fuction to add new projects field
function addNewPField(){
    let newNode = document.createElement("textarea");
    newNode.classList.add("address");
    newNode.setAttribute("name", "project");
    newNode.setAttribute("rows", 3);
    newNode.setAttribute("cols", 30);
    newNode.setAttribute("placeholder", "Write about your Project and Project Description...");

    let projects = document.getElementById("projects");
    let pAddButton = document.getElementById("pAddBtn");

    projects.insertBefore(newNode, pAddButton);
}

// fuction to add new skills field
function addNewSField(){
    let newNode = document.createElement("input");
    newNode.classList.add("skill");
    newNode.setAttribute("type", "text")
    newNode.setAttribute("name", "skill");
    newNode.setAttribute("placeholder", "skill...");

    let skills = document.getElementById("skills");
    let sAddButton = document.getElementById("skillsAddBtn");

    skills.insertBefore(newNode, sAddButton);
}

// fuction to add new achademic qualification field
function addNewAField(){
    let newNode = document.createElement("textarea");
    newNode.classList.add("workexp");
    newNode.setAttribute("name", "workexp");
    newNode.setAttribute("rows", 3);
    newNode.setAttribute("cols", 30);
    newNode.setAttribute("placeholder", "Enter your work experience here...");

    let aq = document.getElementById("aq");
    let weAddButton = document.getElementById("aqAddBtn");

    aq.insertBefore(newNode, weAddButton);
}

function makepdf() {
    window.print();
}