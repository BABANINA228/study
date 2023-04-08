function show(){
    let a = Number(document.getElementById('a').value)
    let b = Number(document.getElementById('b').value)
    let c = Number(document.getElementById('c').value)
    let d = (b*b - 4*a*c)
    document.getElementById('D').value = d
    if(d>0){
        document.getElementById('x1').value = (-b + Math.sqrt(d))/(2*a)
        document.getElementById('x2').value = (-b - Math.sqrt(d))/(2*a)
    }else{
        document.getElementById('x1').value = 'Корней нет'
        document.getElementById('x2').value = 'Корней нет'
    }
}

function cl(){
    document.getElementById('a').value = ''
    document.getElementById('b').value = ''
    document.getElementById('c').value = ''
    document.getElementById('D').value = ''
    document.getElementById('x1').value = ''
    document.getElementById('x2').value = ''
    
}
