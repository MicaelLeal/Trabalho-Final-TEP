import { Component, OnInit } from '@angular/core';
import { Carta } from '../cartas';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cartas',
  templateUrl: './cartas.component.html',
  styleUrls: ['./cartas.component.css']
})
export class CartasComponent implements OnInit {

  cartasUrl = 'http://localhost:8000/cartas/';
  verificarUrl = 'http://localhost:8000/sequencias/'
  cartasList = Array<Carta>();
  cartasSeq = Array<Carta>();
  valido = "Escolha tres cartas";

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get(this.cartasUrl).subscribe(response => this.carregarCartas(response))
  }

  carregarCartas(response) {
    for (const carta of response) {
      this.cartasList.push(new Carta(carta.id, carta.naipe, carta.valor));
    }
    console.log(this.cartasList)
  }

  removerDaSequencia(carta: Carta){
    let index = this.cartasSeq.indexOf(carta);
    console.log(index)
    if (index > -1) {
      this.cartasSeq.splice(index, 1);
   }
  }

  addNaSequencia(carta: Carta) {
    if (this.cartasSeq.length < 3) {
      this.cartasSeq.push(carta);
    }
  }

  liparSequencia() {
    this.cartasSeq = Array<Carta>()
    this.valido = "Escolha tres cartasl";
  }

  verificar() {
    if (this.cartasSeq.length != 3) {
      this.valido = "Por favor, escolha tres cartas!"
      return ;
    }
    let carta1 = this.cartasSeq[0].id
    let carta2 = this.cartasSeq[1].id
    let carta3 = this.cartasSeq[2].id
    this.http.post(this.verificarUrl, {carta1, carta2, carta3})
    .subscribe(response => this.valido = response['validacao'])
  }

}
