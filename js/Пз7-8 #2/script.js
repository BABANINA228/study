function show(sel){
    const select = document.getElementById('tab')
    select.innerHTML = ''
    let formula = sel.options[sel.selectedIndex].text
    let a = parseFloat(document.getElementById('a').value)
    let b = parseFloat(document.getElementById('b').value)
    let h = parseFloat(document.getElementById('h').value)
    let i = 0

    let y = 0
    for (x=a;x<=b;x=x+h){
        switch(formula){
            case 'y = x^2':
                y = x * x
                console.log(y);
                break
            case 'y = x':
                y = x
                console.log(y);
                break
            case 'y = sqrt(x + x)':
                y = Math.sqrt(x + x)
                console.log(y);
                break
        }
        
        var opt = document.createElement('option');
        t = 'x = ' +  Math.round(x * Math.pow(10, 2)) / Math.pow(10, 2) + '  y = ' + Math.round(y * Math.pow(10, 2)) / Math.pow(10, 2)
        opt.value = t;
        opt.innerHTML = t;
        select.appendChild(opt)
        i ++
    }
}

function cl(){
    const select = document.getElementById('tab')
    document.getElementById('a').value = ''
    document.getElementById('b').value = ''
    document.getElementById('h').value = ''
    select.innerHTML = ''
}
