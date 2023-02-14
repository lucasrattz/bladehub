async function getApi(type) {
    const api = `http://localhost:2774/api/${type}`;

    const response = await fetch(api);
    let data = await response.json();
    console.log(data);

    display(parse(data));
}

function display(data) {
    document.getElementById("generated-content").innerHTML = data;
}

function parse(data) {
    const content = data["description"];
    return content.replace(/(?:\r\n|\r|\n)/g, '<br/>');
}

