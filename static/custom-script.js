//responsible for calling the tableau maps
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsidePolicyMandates: {
        initPolicyMandatesMap: function () {
            var viz;
            var vizContainer = document.getElementById("tableauPolicyMandatesMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '400px',
//                 hideTabs: true,
//                 hideToolbar: true,
//                 onFirstInteraction: function() {
//                     console.log("run something after the first interaction!");
//                 }
            };
            viz = new tableau.Viz(vizContainer, url, options);
            console.log("initPolicyMandatesMap is run");
//             return viz
        }
    }
});
// window.onload = () => {
//     initViz();
//     console.log("window onload is run");
// }

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideReliefFunding: {
        initReliefFundingMap: function () {
            var viz;
            var vizContainer = document.getElementById("tableauReliefFundingMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '400px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz = new tableau.Viz(vizContainer, url, options);
            console.log("initReliefFundingMap is run");
        }
    }
});

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideDemographics: {
        initDemographicsMap: function () {
            var viz;
            var vizContainer = document.getElementById("tableauDemographicsMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '400px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz = new tableau.Viz(vizContainer, url, options);
            console.log("initDemographicsMap is run");
        }
    }
});

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideOverview: {
        initOverviewMap: function () {
            var viz;
            var vizContainer = document.getElementById("tableauOverviewMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '400px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz = new tableau.Viz(vizContainer, url, options);
            console.log("initOverviewMap is run");
        }
    }
});