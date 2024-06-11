function callback(json)
{
    let element = document.getElementById("like"+json.id);
    let element2 = document.getElementById("heart"+json.id);
    element.textContent = json.like;
    console.log(json.id);
    if (json.flag == 1)
        element2.textContent = '❤';
    else
        element2.textContent = '💗';
}

function callback2(json)
{
    let element = document.getElementById("like2"+json.id);
    let element2 = document.getElementById("heart2"+json.id);
    element.textContent = json.like;
    if (json.flag == 1)
        element2.textContent = '❤'
    else
        element2.textContent = '💗'
}

function like(user_id, tweet_id)
{
    fetch('/api/tweet/' + user_id + '/' + tweet_id + '/like')
    .then(response => response.json())
    .then(callback)
}

function like2(user_id, reply_id)
{
    fetch('/api/reply/' + user_id + '/' + reply_id + '/like')
    .then(response => response.json())
    .then(callback2)
}
