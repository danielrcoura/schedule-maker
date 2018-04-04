var scheduleMaker = angular.module("scheduleMakerApp", []);

scheduleMaker.controller('controller', function($scope, $http){
	$scope.title = "Schedule Maker";
	var horarios;
	getHorarios();

	function getHorarios () {
		$http.get('http://127.0.0.1:8000/assets/horarios.json')
		.then(function successCallback(data) {
			horarios = data;
			console.log(horarios);
		}, function (error) {
			console.log(error);
		});
	}
});