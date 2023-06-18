pragma solidity ^0.8.19;
// SPDX-License-Identifier: MIT

contract Loteria {
    // array de direcciones de monederos
    address[] public players;
    // cantidad de ETH del premio
    uint public prizeAmount; 

    constructor() payable {
        //precio de creacion de loteria
        require(msg.value >= 10 wei, "La cantidad de 10 WEI enviada no coincide con el premio establecido");
        // prizeAmount = msg.value;
    }

    function enter() public payable {
        //Coste de participacion
        require(msg.value == 1 wei, "Se requiere 1 WEI para entrar en la loteria");

        //Agregamos el jugador al Array de jugadores.
        players.push(msg.sender);

        //Añadimos el conste de la participacion para el bote total del premio.
        prizeAmount += (msg.value);

    }

    function random() private view returns (uint) {
        //Dependiendo del bloque en el que se ejecute el script sera necesario cambiar el nombre de algunos de los parametros, en este caso "difficulty"

        //return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players.length)));
        return uint(keccak256(abi.encodePacked(block.prevrandao, block.timestamp, players.length)));
        
    }

    function pickWinner() public payable {
        require(players.length > 0, "No hay jugadores en la loteria");

        uint index = random() % players.length;
        address payable winner = payable(players[index]);

        //Transferimos el premio al ganador.
        winner.transfer(prizeAmount);

        // reinicializar el contrato para el siguiente sorteo
        players = new address[](0);
        prizeAmount = 0;
    }
}
