const twitter_data = require('../../data/TwitterData/tweets.json');
const reddit_data = require('../../data/RedditData/headlines.json');
const profile = require('../../data/profile.json');

let twitter_count = 0; //number of tweets generated
document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
let reddit_count = 0; //number of posts generated
document.getElementById("number_of_reddit_results").innerHTML = reddit_count + ' results';
let total_count = 0; //total number of tweets and posts generated
document.getElementById("number_of_results").innerHTML = total_count + ' results';

/* css-styled html for each tweet result that appears on the page */
function tweet_html(html) {
    return '<div class="tweet">' +
        '<i class="fab fa-twitter"></i>' +
        '<br>' +
        '<div class="tweet_text_box">' +
        '<p class="tweet_text">' + html.rawText + '</p>' +
        '</div>' +
        '<br>' +
        '</div>' +
        '<br>';
}

/* tweet output (html, results numbers) generated from filtering data */
function twitter_output(output) {
    document.getElementById("Twitter").innerHTML = output;
    document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
    total_count += twitter_count;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

/* returns tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_results() {
    let output = "";
    function readTweetData(data) {
        for (let tweet of data) {
            twitter_count++;
            output += tweet_html(tweet);
        }
    }

    readTweetData(twitter_data);
    twitter_output(output);
}

/* returns positive sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_positive_results() {
    let output = "";
    function readPositiveTweetData(data) {
        for (let tweet of data) {
            if(tweet.polarity != null) {
                if(tweet.polarity > 0.0) {
                    twitter_count++;
                    output += tweet_html(tweet);
                }
            }
        }
    }

    readPositiveTweetData(twitter_data);
    twitter_output(output);
}

/* returns negative sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_negative_results() {
    let output = "";
    function readNegativeTweetData(data) {
        for (let tweet of data) {
            if(tweet.polarity != null) {
                if(tweet.polarity < 0.0) {
                    twitter_count++;
                    output += tweet_html(tweet);
                }
            }
        }
    }

    readNegativeTweetData(twitter_data);
    twitter_output(output);
}

/* returns neutral sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_neutral_results() {
    let output = "";
    function readNeutralTweetData(data) {
        for (let tweet of data) {
            if(tweet.polarity != null) {
                if(tweet.polarity === 0.0) {
                    twitter_count++;
                    output += tweet_html(tweet);
                }
            }
        }
    }

    readNeutralTweetData(twitter_data);
    twitter_output(output);
}


/* css-styled html for each post result that appears on the page */
function post_html(html) {
    return '<div class="post">' +
        '<i class="fab fa-reddit"></i>' +
        '<br>' +
        '<div class="post_text_box">' +
        '<p class="post_text">' + html.headline + '</p>' +
        '</div>' +
        '<br>' +
        '</div>' +
        '<br>';
}

/* post output (html, results numbers) generated from filtering data */
function reddit_output(output) {
    document.getElementById("Reddit").innerHTML = output;
    document.getElementById("number_of_reddit_results").innerHTML = reddit_count + ' results';
    total_count += reddit_count;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

/* returns posts and result numbers for any post that contains the chosen input as a substring */
function reddit_results() {
    let output = "";
    function readPostData(data) {
        for (let post of data) {
            reddit_count++;
            output += post_html(post);
        }
    }

    readPostData(reddit_data);
    reddit_output(output);
}

/* returns positive sentiment posts and result numbers for any post that contains the chosen input as a substring */
function reddit_positive_results() {
    let output = "";
    function readPostivePostData(data) {
        for (let post of data) {
            if(post.compound != null) {
                if(post.compound > 0.0) {
                    reddit_count++;
                    output += post_html(post);
                }
            }
        }
    }

    readPostivePostData(reddit_data);
    reddit_output(output);
}

/* returns negative sentiment posts and result numbers for any post that contains the chosen input as a substring */
function reddit_negative_results() {
    let output = "";
    function readNegativePostData(data) {
        for (let post of data) {
            if(post.compound != null) {
                if(post.compound < 0.0) {
                    reddit_count++;
                    output += post_html(post);
                }
            }
        }
    }

    readNegativePostData(reddit_data);
    reddit_output(output);
}

/* returns neutral sentiment posts and result numbers for any post that contains the chosen input as a substring */
function reddit_neutral_results() {
    let output = "";
    function readNeutralPostData(data) {
        for (let post of data) {
            if(post.compound != null) {
                if(post.compound === 0.0) {
                    reddit_count++;
                    output += post_html(post);
                }
            }
        }
    }

    readNeutralPostData(reddit_data);
    reddit_output(output);
}


/* clears html and resets result numbers/counts to 0 */
function clear() {
    document.getElementById("Profile").innerHTML = '';
    document.getElementById("Twitter").innerHTML = '';
    twitter_count = 0;
    document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
    document.getElementById("Reddit").innerHTML = '';
    reddit_count = 0;
    document.getElementById("number_of_reddit_results").innerHTML = reddit_count + ' results';
    total_count = 0;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

function profile_html(){
    return '<div class="infobox">' +
                '<div class="banner">' +
                    '<a href="https://en.wikipedia.org/wiki/' + profile.name + '" class="fn main_text">' + profile.name + '</a>' +
                '</div>' +
                '<img src=' + profile.image + ' alt="profile_image">' +
                '<br>' +
                '<div class="banner">' +
                    '<span class="main_text">Personal details</span>' +
                '</div>' +
                '<p class="main_text">Age:</p> <p class="content">' + profile.age + '</p>' +
                '<br>' +
                '<p class="main_text">Political Party:</p> <p class="content">' + profile.party + '</p>' +
            '</div>' +
            profile.summary +
            '<br>' +
            '<h2 class="fn main_text"> Twitter Plot Data </h2>' +
            '<br>' +
            '<img src="../assets/twitter_plot_data.png" alt="twitter_plot_data">' +
            '<br>' +
            '<h2 class="fn main_text"> Reddit Plot Data </h2>' +
            '<br>' +
            '<img src="../assets/reddit_plot_data.png" alt="reddit_plot_data">' +
            '<br>' +
            '<h2 class="fn main_text"> Combined Plot Data </h2>' +
            '<br>' +
            '<img src="../assets/combined_plot_data.png" alt="combined_plot_data">';
}

/* enables search after typing in input and clicking on the search button */
window.onload = function() {
    clear();
    document.getElementById("Profile").innerHTML = profile_html();
    twitter_results();
    openTab(event, 'Profile');
    reddit_results();
    window.scrollTo(0, 0);
};

/* allows for switching through tabs */
function openTab(event, tabName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}
document.getElementById('profile_tab').onclick=function() {openTab(event, 'Profile');};
document.getElementById('twitter_tab').onclick=function() {openTab(event, 'Twitter');};
document.getElementById('reddit_tab').onclick=function() {openTab(event, 'Reddit');};


/* filters search results by positive sentimentality on form press */
document.getElementById('positive').onchange=function(){
    clear();
    document.getElementById("Profile").innerHTML = profile_html();
    twitter_positive_results();
    openTab(event, 'Twitter');
    reddit_positive_results();
};

/* filters search results by negative sentimentality on form press */
document.getElementById('negative').onchange=function(){
    clear();
    document.getElementById("Profile").innerHTML = profile_html();
    twitter_negative_results();
    openTab(event, 'Twitter');
    reddit_negative_results()
};

/* filters search results by neutral sentimentality on form press */
document.getElementById('neutral').onchange=function(){
    clear();
    document.getElementById("Profile").innerHTML = profile_html();
    twitter_neutral_results();
    openTab(event, 'Twitter');
    reddit_neutral_results()
};

window.onscroll=function(){
    let topnav = document.getElementById("topnav");
    topnav.style.position = 'fixed';
    topnav.style.width = '-webkit-fill-available';
    let body = document.body;
    let doc_elem = document.documentElement;
    doc_elem = (doc_elem.clientHeight)? doc_elem : body;

    if (doc_elem.scrollTop === 0) {
        topnav.style.position = '';
        topnav.style.width = '';
    }
};
