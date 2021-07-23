// function initializeViz() {
//   // JS object that points at empty div in the html
//   var placeholderDiv = document.getElementById("tableauViz");
//   // URL of the viz to be embedded
//   var url = "http://public.tableau.com/views/WorldIndicators/GDPpercapita";
//   // An object that contains options specifying how to embed the viz
//   var options = {
//     width: '600px',
//     height: '600px',
//     hideTabs: true,
//     hideToolbar: true,
//   };
//   viz = new tableau.Viz(placeholderDiv, url, options);
// }

function initViz() {
    
    var containerDiv = document.getElementById("tableauViz"),
//     url = "https://prod-useast-b.online.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link";
//     https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js
//     url='https://prod-useast-b.online.tableau.com/t/ds4ateam79covid/views/Covid-19Analysis-Gathering_Bans';
    url='https://prod-useast-b.online.tableau.com/t/ds4ateam79covid/views/Covid-19Analysis-Gathering_Bans/BansperCounty';
    var options = {
        width: '450px',
        height: '450px',
        site_root: '&#47;t&#47;ds4ateam79covid',
        name: 'Covid-19Analysis-Gathering_Bans&#47;BansperCounty&#47;andyceldo1@gmail.com&#47;6f2769cf-927e-4dd6-a235-370d1e74ed21',
        hideTabs: false,
        hideToolbar: false,
        onFirstInteraction: function() {
            console.log("run something after the first interaction!");
        }
    };
    var viz = new tableau.Viz(containerDiv, url, options);
    console.log("initViz is run");
}
initViz();