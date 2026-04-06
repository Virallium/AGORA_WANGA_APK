window.addEventListener('load', ()=>{
    const loading_container=document.querySelector('.loading')
    const loading_circle=document.querySelector('.loading .circle ')
    const loading_circle_img=document.querySelector('.loading .circle img')
    loading_container.classList.add('removeloading')
    loading_circle.classList.add('removeloadingcircle')
    loading_circle_img.classList.add('removeloadingimg')
})