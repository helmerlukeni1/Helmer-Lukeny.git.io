function somar(){
      var tn1=window.document.getElementById("text1")
      var tn2=window.document.getElementById("text2")
      var res=window.document.getElementById("res")
      var n1=Number(tn1.value)
      var n2=Number(tn2.value)
      var s= n1 + n2
      res.innerHTML= s
      
    }
    
    const nota1=15
    const nota2=10
    const media= (nota1 + nota2) /2
    console.log("A nota do aluno é:" +media)
    
    const notaFinal= 12.5
    if (notaFinal>=10){
      console.log("Parabéns! Estás Aprovado")
    } else{
      console.log("Estude mais! Estás Reprovado")
    }