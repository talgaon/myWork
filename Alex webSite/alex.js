var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// This function creates an <iframe> (and YouTube player) after the API code downloads.
var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: 'exL6a187R1w',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange

      }
  });
}
function changevid(){
  player.loadVideoById({videoId: 'MRAZ_mSLXrA'
});
}




     function onPlayerStateChange(event) {
       if(event.data == YT.PlayerState.ENDED){
         player.destroy()
       }
     }

function original(){
  player.loadVideoById({videoId: 'exL6a187R1w'
});
}

function other(){
  player.loadVideoById({videoId: 'y2xyq6vsL08'
});
}

// The API will call this function when the video player is ready.
function onPlayerReady(event) {
   //event.target.playVideo();
}

function play(){
  player.playVideo()
}

function pause(){
  player.pauseVideo()
}
