const twdata = require('../../data/twData/booker_tweets');
const twdata1 = require('../../data/twData/christie_tweets');
const twdata2 = require('../../data/twData/clinton_tweets');
const twdata3 = require('../../data/twData/cruz_tweets');
const twdata4 = require('../../data/twData/obama_tweets');
const twdata5 = require('../../data/twData/sanders_tweets');
const twdata6 = require('../../data/twData/trump_tweets');
const fbdata = require('../../data/oldFbdata/fbdata.json');
const fbdata1 = require('../../data/oldFbdata/fbdata1.json');

function openTab(event, siteName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(siteName).style.display = "block";
    event.currentTarget.className += " active";
}

let total_count = 0;
document.getElementById("number_of_results").innerHTML = total_count + ' results';
let twitter_count = 0;
document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
let facebook_count = 0;
document.getElementById("number_of_facebook_results").innerHTML = facebook_count + ' results';
let reddit_count = 0;
document.getElementById("number_of_reddit_results").innerHTML = reddit_count + ' results';

function twitter_results() {
    let stdin = document.getElementById("search_input").value;
    let output = "";
    function readTweetData(data) {
        for (let tweet of data) {
            if(tweet.rawText != null) {
                if(tweet.rawText.toUpperCase().includes(stdin.toUpperCase())) {
                     twitter_count++;
                     output +=
                     '<div class="tweet">' +
                     '<i class="fab fa-twitter"></i>' +
                     '<br>' +
                     '<div class="tweet_text_box">' +
                     '<p class="tweet_text">' + tweet.rawText + '</p>' +
                     '</div>' +
                     '<br>' +
                     '</div>' +
                     '<br>';
                }
            }
        }
    }

    readTweetData(twdata);
    readTweetData(twdata1);
    readTweetData(twdata2);
    readTweetData(twdata3);
    readTweetData(twdata4);
    readTweetData(twdata5);
    readTweetData(twdata6);

    document.getElementById("Twitter").innerHTML = output;
    document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
    total_count += twitter_count;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

function facebook_results() {
    let stdin = document.getElementById("search_input").value;
    let output = "";
    function readFbData(data) {
        for (let post of data) {
            if(post.Comment != null) {
                if(post.Comment.toUpperCase().includes(stdin.toUpperCase())) {
                    facebook_count++;
                    output +=
                        '<div class="fb_comment">' +
                        '<i class="fab fa-facebook"></i>' +
                        '<br>' +
                        '<div class="fb_comment_text_box">' +
                        '<p class="fb_comment_text">' + post.Comment + '</p>' +
                        '</div>' +
                        '<br>' +
                        '</div>' +
                        '<br>';
                }
            }
        }
    }

    readFbData(fbdata);
    readFbData(fbdata1);

    document.getElementById("Facebook").innerHTML = output;
    document.getElementById("number_of_facebook_results").innerHTML = facebook_count + ' results';
    total_count += facebook_count;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

document.getElementById('search_button').onclick=function() {
    twitter_results();
    openTab(event, 'Twitter');
    facebook_results()
}; //search after clicking on button

let input = document.getElementById("search_input");
input.addEventListener("keyup", function(event) { //search after pressing enter
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("search_button").click();
    }
});

document.getElementById('twitter_tab').onclick=function() {openTab(event, 'Twitter');};
document.getElementById('facebook_tab').onclick=function() {openTab(event, 'Facebook');};
document.getElementById('reddit_tab').onclick=function() {openTab(event, 'Reddit');};