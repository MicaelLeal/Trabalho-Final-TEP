var valores = Array<number>()

export class Carta {
    constructor(public id, public naipe, public valor) {   }

    get clas_css() {
        if (this.valor == 10) {
            return "ten_"+this.naipe;
        }
        if (this.valor == 9) {
            return "nine_"+this.naipe;
        }
        if (this.valor == 8) {
            return "eight_"+this.naipe;
        }
        if (this.valor == 7) {
            return "seven_"+this.naipe;
        }
        if (this.valor == 6) {
            return "six_"+this.naipe;
        }
        if (this.valor == 5) {
            return "five_"+this.naipe;
        }
        if (this.valor == 4) {
            return "four_"+this.naipe;
        }
        if (this.valor == 3) {
            return "three_"+this.naipe;
        }
        if (this.valor == 2) {
            return "two_"+this.naipe;
        }
        return this.valor+"_"+this.naipe;
    }
}