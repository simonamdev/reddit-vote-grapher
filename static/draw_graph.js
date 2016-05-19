function drawGraph(plotData) {
	var score = [];
	var up = [];
	var down = [];
	var ratio = [];
	plotData.forEach(function(item, index) {
		score.push({x: item[0], y: item[1]});
		up.push({x: item[0], y: item[2]});
		down.push({x: item[0], y: item[3]});
		ratio.push({x: item[0], y: item[4]});
	});
	drawAll(score, up, down, ratio);
	drawScore(score);
	drawUp(up);
	drawDown(down);
	drawRatio(ratio);
}

function drawAll(dataScore, dataUp, dataDown, dataRatio) {
	var container = document.getElementById('visualization-all');
	var groups = new vis.DataSet();

	groups.add({
    id: 0,
    content: 'score'
	});

	groups.add({
    id: 1,
    content: 'up'
	});

	groups.add({
    id: 2,
    content: 'down'
	});

	groups.add({
    id: 3,
    content: 'ratio'
	});

	items = [];

	dataScore.forEach(function(item, index) {
		if (item.y < 0) {
			item.y = 0;
		}
		items.push({x: item.x, y: item.y, group: 0});
	});

	dataUp.forEach(function(item, index) {
		if (item.y < 0) {
			item.y = 0;
		}
		items.push({x: item.x, y: item.y, group: 1});
	});

	dataDown.forEach(function(item, index) {
		if (item.y < 0) {
			item.y = 0;
		}
		items.push({x: item.x, y: item.y, group: 2});
	});

	dataRatio.forEach(function(item, index) {
		if (item.y < 0) {
			item.y = 0;
		}
		items.push({x: item.x, y: item.y, group: 3});
	});

	var dataset = new vis.DataSet(items);
	var options = {
    legend: {
      left: {
        position:"bottom-right"
      }
    },
		shaded: true,
		drawPoints: false
	};
	var graph2d = new vis.Graph2d(container, dataset, groups, options);
}

function drawUp(dataUp) {
	var container = document.getElementById('visualization-up');
	var dataset = new vis.DataSet(dataUp);
	var options = {
		shaded: true,
		drawPoints: false,
		dataAxis: {

		}
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
}

function drawScore(dataScore) {
	var container = document.getElementById('visualization-score');
	var dataset = new vis.DataSet(dataScore);
	var options = {
		shaded: true,
		drawPoints: false
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
}

function drawUp(dataUp) {
	var container = document.getElementById('visualization-up');
	var dataset = new vis.DataSet(dataUp);
	var options = {
		shaded: true,
		drawPoints: false
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
}

function drawDown(dataDown) {
	var container = document.getElementById('visualization-down');
	var dataset = new vis.DataSet(dataDown);
	var options = {
		shaded: true,
		drawPoints: false
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
}

function drawRatio(dataRatio) {
	var container = document.getElementById('visualization-ratio');
	var dataset = new vis.DataSet(dataRatio);
	var options = {
		shaded: true,
		drawPoints: false
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
}

function testVariables(plotData) {
	var score = [];
	var up = [];
	var down = [];
	var ratio = [];
	plotData.forEach(function(item, index) {
		score.push({x: item[0], y: item[1]});
		up.push({x: item[0], y: item[2]});
		down.push({x: item[0], y: item[3]});
		ratio.push({x: item[0], y: item[4]});
	});
	console.log(score[score.length - 1].y);
}

