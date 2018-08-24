// This code loads the IFrame Player API code asynchronously.
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
    videoId: 'Gh9Dv5D5aCM',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange

      }
  });
}
function changevid(){
  player.loadVideoById({videoId: '8aQRq9hhekA'
});
}




     function onPlayerStateChange(event) {
       if(event.data == YT.PlayerState.ENDED){
         player.destroy()
       }
     }

function original(){
  player.loadVideoById({videoId: 'Gh9Dv5D5aCM'
});
}

function other(){
  player.loadVideoById({videoId: 'bx9J9EBDTpE'
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
