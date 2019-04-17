const twdata = require('../../data/twData/booker_tweets');
const twdata1 = require('../../data/twData/christie_tweets');
const twdata2 = require('../../data/twData/clinton_tweets');
const twdata3 = require('../../data/twData/cruz_tweets');
const twdata4 = require('../../data/twData/obama_tweets');
const twdata5 = require('../../data/twData/sanders_tweets');
const twdata6 = require('../../data/twData/trump_tweets');
const fbdata = require('../../data/oldFbdata/fbdata.json');
const fbdata1 = require('../../data/oldFbdata/fbdata1.json');

let twitter_count = 0; //number of tweets generated
document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
let facebook_count = 0; //number of facebook comments generated
document.getElementById("number_of_facebook_results").innerHTML = facebook_count + ' results';
let reddit_count = 0; //number of reddit posts generated
document.getElementById("number_of_reddit_results").innerHTML = reddit_count + ' results';
let total_count = 0; //total number of tweets, comments and posts generated
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
function twitter_results(typed_input) {
    let output = "";
    function readTweetData(data) {
        for (let tweet of data) {
            if(tweet.rawText != null) {
                if(tweet.rawText.toUpperCase().includes(typed_input.toUpperCase())) {
                     twitter_count++;
                     output += tweet_html(tweet);
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
    twitter_output(output);
}

/* returns positive sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_positive_results(typed_input) {
    let output = "";
    function readPositiveTweetData(data) {
        for (let tweet of data) {
            if(tweet.rawText != null) {
                if(tweet.polarity != null) {
                    if(tweet.polarity > 0 && tweet.rawText.toUpperCase().includes(typed_input.toUpperCase())) {
                        twitter_count++;
                        output += tweet_html(tweet);
                    }
                }
            }
        }
    }

    readPositiveTweetData(twdata);
    readPositiveTweetData(twdata1);
    readPositiveTweetData(twdata2);
    readPositiveTweetData(twdata3);
    readPositiveTweetData(twdata4);
    readPositiveTweetData(twdata5);
    readPositiveTweetData(twdata6);
    twitter_output(output);
}

/* returns negative sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_negative_results(typed_input) {
    let output = "";
    function readNegativeTweetData(data) {
        for (let tweet of data) {
            if(tweet.rawText != null) {
                if(tweet.polarity != null) {
                    if(tweet.polarity < 0 && tweet.rawText.toUpperCase().includes(typed_input.toUpperCase())) {
                        twitter_count++;
                        output += tweet_html(tweet);
                    }
                }
            }
        }
    }

    readNegativeTweetData(twdata);
    readNegativeTweetData(twdata1);
    readNegativeTweetData(twdata2);
    readNegativeTweetData(twdata3);
    readNegativeTweetData(twdata4);
    readNegativeTweetData(twdata5);
    readNegativeTweetData(twdata6);
    twitter_output(output);
}

/* returns neutral sentiment tweets and result numbers for any tweet that contains the chosen input as a substring */
function twitter_neutral_results(typed_input) {
    let output = "";
    function readNeutralTweetData(data) {
        for (let tweet of data) {
            if(tweet.rawText != null) {
                if(tweet.polarity != null) {
                    if(tweet.polarity === 0 && tweet.rawText.toUpperCase().includes(typed_input.toUpperCase())) {
                        twitter_count++;
                        output += tweet_html(tweet);
                    }
                }
            }
        }
    }

    readNeutralTweetData(twdata);
    readNeutralTweetData(twdata1);
    readNeutralTweetData(twdata2);
    readNeutralTweetData(twdata3);
    readNeutralTweetData(twdata4);
    readNeutralTweetData(twdata5);
    readNeutralTweetData(twdata6);
    twitter_output(output);
}


/* css-styled html for each facebook comment result that appears on the page */
function fb_comment_html(html) {
    return '<div class="fb_comment">' +
        '<i class="fab fa-facebook"></i>' +
        '<br>' +
        '<div class="fb_comment_text_box">' +
        '<p class="fb_comment_text">' + html.Comment + '</p>' +
        '</div>' +
        '<br>' +
        '</div>' +
        '<br>';
}

/* comment output (html, results numbers) generated from filtering data */
function facebook_output(output) {
    document.getElementById("Facebook").innerHTML = output;
    document.getElementById("number_of_facebook_results").innerHTML = facebook_count + ' results';
    total_count += facebook_count;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

/* returns comments and result numbers for any tweet that contains the chosen input as a substring */
function facebook_results(typed_input) {
    let output = "";
    function readFbData(data) {
        for (let post of data) {
            if(post.Comment != null) {
                if(post.Comment.toUpperCase().includes(typed_input.toUpperCase())) {
                    facebook_count++;
                    output += fb_comment_html(post);
                }
            }
        }
    }

    readFbData(fbdata);
    readFbData(fbdata1);
    facebook_output(output);
}

/* returns positive sentiment comments and result numbers for any comment that contains the chosen input as a substring */
function facebook_positive_results(typed_input) {
    let output = "";
    function readPostiveFbData(data) {
        for (let post of data) {
            if(post.Comment != null) {
                if(post.Positive != null && post.Negative != null) {
                    if(post.Positive > post.Negative && post.Comment.toUpperCase().includes(typed_input.toUpperCase())) {
                        facebook_count++;
                        output += fb_comment_html(post);
                    }
                }
            }
        }
    }

    readPostiveFbData(fbdata);
    readPostiveFbData(fbdata1);
    facebook_output(output);
}

/* returns negative sentiment comments and result numbers for any comment that contains the chosen input as a substring */
function facebook_negative_results(typed_input) {
    let output = "";
    function readNegativeFbData(data) {
        for (let post of data) {
            if(post.Comment != null) {
                if(post.Positive != null && post.Negative != null) {
                    if(post.Positive < post.Negative && post.Comment.toUpperCase().includes(typed_input.toUpperCase())) {
                        facebook_count++;
                        output += fb_comment_html(post);
                    }
                }
            }
        }
    }

    readNegativeFbData(fbdata);
    readNegativeFbData(fbdata1);
    facebook_output(output);
}


/* clears html and resets result numbers/counts to 0 */
function clear() {
    document.getElementById("Twitter").innerHTML = '';
    twitter_count = 0;
    document.getElementById("number_of_twitter_results").innerHTML = twitter_count + ' results';
    document.getElementById("Facebook").innerHTML = '';
    facebook_count = 0;
    document.getElementById("number_of_facebook_results").innerHTML = facebook_count + ' results';
    total_count = 0;
    document.getElementById("number_of_results").innerHTML = total_count + ' results';
}

/* enables search after typing in input and clicking on the search button */
document.getElementById('search_button').onclick=function() {
    clear();
    let typed_input = document.getElementById("search_input").value;
    twitter_results(typed_input);
    openTab(event, 'Twitter');
    facebook_results(typed_input)
};

/* enables search from pressing the enter key */
let input = document.getElementById("search_input");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("search_button").click();
    }
});

/* allows for switching through tabs */
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
document.getElementById('twitter_tab').onclick=function() {openTab(event, 'Twitter');};
document.getElementById('facebook_tab').onclick=function() {openTab(event, 'Facebook');};
document.getElementById('reddit_tab').onclick=function() {openTab(event, 'Reddit');};


/* filters search results by positive sentimentality on form press */
document.getElementById('positive').onchange=function(){
    clear();
    let typed_input = document.getElementById("search_input").value;
    twitter_positive_results(typed_input);
    openTab(event, 'Twitter');
    facebook_positive_results(typed_input)
};

/* filters search results by negative sentimentality on form press */
document.getElementById('negative').onchange=function(){
    clear();
    let typed_input = document.getElementById("search_input").value;
    twitter_negative_results(typed_input);
    openTab(event, 'Twitter');
    facebook_negative_results(typed_input)
};

/* filters search results by neutral sentimentality on form press */
document.getElementById('neutral').onchange=function(){
    clear();
    let typed_input = document.getElementById("search_input").value;
    twitter_neutral_results(typed_input);
    openTab(event, 'Twitter')
};
