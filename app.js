var scheduleMaker = angular.module("scheduleMakerApp", []);

scheduleMaker.controller('controller', function($scope, $http){
	var URL = 'http://127.0.0.1:8000';
	$scope.disciplinas;
	$scope.selecionadas;
	$scope.horariosSelecionados;

	var horarios;
	getHorarios();
	getDisciplinas();

	function getHorarios () {
		$http.get(URL + '/assets/horarios.json')
		.then(function successCallback(data) {
			horarios = data.data;
			console.log(horarios);
		}, function errorCallback(error) {
			console.log(error);
		});
	}

	function getDisciplinas () {
		$http.get(URL + '/assets/disciplinas.json')
		.then(function successCallback(data) {
			$scope.disciplinas = data.data;
			console.log($scope.disciplinas);
		}, function errorCallback(error) {
			console.log(error);
		});
	}

	$scope.selectDiscipline = function (discipline) {
		$scope.disciplinas[discipline].selected = !$scope.disciplinas[discipline].selected;
		getDisciplinasSelecionadas();
	}

	function getDisciplinasSelecionadas() {
		$scope.horariosSelecionados =  horarios.filter(function (disc) {
			if ($scope.disciplinas[disc['nome']].selected)  {
				return disc;
			}
		})
	}

	$scope.setTurma = function (disciplina) {
		disciplina.turma += 1;
		console.log(disciplina.turma);
	}

});