function AfficherMenu(){
    const menu=document.querySelector('#menu_bar')
    const closed_bar=document.querySelector('#closed_bar')
    const nav=document.querySelector('nav ul')
     const rgba=document.querySelector('.rgba')
    menu.addEventListener('click',()=>{
        nav.classList.add('activemenu')
        rgba.classList.add('rgbaactive')
    })
    closed_bar.addEventListener('click',()=>{
        nav.classList.remove('activemenu')
        rgba.classList.remove('rgbaactive')
    })
    rgba.addEventListener('click',()=>{
        nav.classList.remove('activemenu')
        rgba.classList.remove('rgbaactive')
    })
    
}
AfficherMenu()