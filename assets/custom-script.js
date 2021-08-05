var viz_policy, viz_relief, viz_demographics, viz_overview, viz_line_graph;

//responsible for calling the tableau maps
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsidePolicyMandates: {
        initPolicyMandatesMap: function () {
            if(!viz_policy == null) {
                viz_policy.dispose();
            }
            var vizContainer = document.getElementById("tableauPolicyMandatesMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '500px',
//                 hideTabs: true,
//                 hideToolbar: true,
//                 onFirstInteraction: function() {
//                     console.log("run something after the first interaction!");
//                 }
            };
            viz_policy = new tableau.Viz(vizContainer, url, options);
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
//             var viz;
            if(!viz_relief == null) {
                viz_relief.dispose();
            }
            var vizContainer = document.getElementById("tableauReliefFundingMap"),    
            url = 'https://public.tableau.com/views/Covid-19_Analysis_Relief_Funding/ReliefFunding',
            options = {
                width: '100%',
                height: '500px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz_relief = new tableau.Viz(vizContainer, url, options);
            console.log("initReliefFundingMap is run");
        }
    }
});

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideDemographics: {
        initDemographicsMap: function () {
            if(!viz_demographics == null) {
                viz_demographics.dispose();
            }
            var vizContainer = document.getElementById("tableauDemographicsMap"),    
            url = 'https://public.tableau.com/views/Covid-19_Analysis_Relief_Funding/ReliefFunding',
            options = {
                width: '100%',
                height: '500px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz_demographics = new tableau.Viz(vizContainer, url, options);
            console.log("initDemographicsMap is run");
        }
    }
});

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideOverview: {
        initOverviewMap: function () {
            if(!viz_overview == null) {
                viz_overview.dispose();
            }
            var vizContainer = document.getElementById("tableauOverviewMap"),    
            url = 'https://public.tableau.com/views/Covid-19Analysis-Gathering_Bans/BansperCounty',
            options = {
                width: '100%',
                height: '500px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz_overview = new tableau.Viz(vizContainer, url, options);
            console.log("initOverviewMap is run");
        }
    }
});

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientsideTableauLineGraph: {
        initTableauLineGraph: function () {
            if(!viz_line_graph == null) {
                viz_line_graph.dispose();
            }
            var vizContainer = document.getElementById("tableauLineGraph"),    
            url = 'https://public.tableau.com/views/Covid-19AnalysiswithMonthsLineGraph/Covid-19overMonths',
            options = {
                width: '100%',
                height: '500px',
                hideTabs: false,
                hideToolbar: false,
            };
            viz_line_graph = new tableau.Viz(vizContainer, url, options);
            console.log("initTableauLineGraph is run");
        }
    }
});