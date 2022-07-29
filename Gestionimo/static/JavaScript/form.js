function mynext() {
    const form = document.getElementById('next');
    const Prod = document.getElementById('produit');
    const comm = document.getElementById('commentaire');
    const phot = document.getElementById('photos');
    const check = document.getElementById('check');
    const ged = document.getElementById('ged');
  
      // 👇️ this SHOWS the form
      form.style.display = 'block';
      check.style.display = 'block';
      Prod.style.display = 'none';
      comm.style.display = 'none';
      ged.style.display = 'none';
      phot.style.display = 'none';
            };
 
  function mynext1(){
    const form = document.getElementById('next');
    const Prod = document.getElementById('produit');
    const comm = document.getElementById('commentaire');
    const phot = document.getElementById('photos');
    const check = document.getElementById('check');
    const ged = document.getElementById('ged');
  
   
       form.style.display = 'none';
       check.style.display = 'none';
       phot.style.display = 'none';
       ged.style.display = 'none';
       Prod.style.display = 'block';
       comm.style.display = 'none';
  };
        
  function commentaire(){
    const form = document.getElementById('next');
    const Prod = document.getElementById('produit')
    const comm = document.getElementById('commentaire');
    const phot = document.getElementById('photos');
    const check = document.getElementById('check');
    const ged = document.getElementById('ged');
  
       Prod.style.display= 'none ';
       form.style.display = 'none';
       phot.style.display = 'none';
       check.style.display = 'none';
       ged.style.display = 'none';
       comm.style.display = 'block';
  };
 
  function photo(){
    const form = document.getElementById('next');
    const Prod = document.getElementById('produit');
    const comm = document.getElementById('commentaire');
    const phot = document.getElementById('photos');
    const check = document.getElementById('check');
    const ged = document.getElementById('ged');
  
       Prod.style.display= 'none ';
       form.style.display = 'none';
       comm.style.display = 'none';
       check.style.display = 'none';
       ged.style.display = 'none';
       phot.style.display = 'block';
  };

  function ged(){
    const form = document.getElementById('next');
    const Prod = document.getElementById('produit');
    const comm = document.getElementById('commentaire');
    const phot = document.getElementById('photos');
    const check = document.getElementById('check');
    const ged = document.getElementById('ged');
  
       Prod.style.display= 'none ';
       form.style.display = 'none';
       comm.style.display = 'none';
       check.style.display = 'none';
       phot.style.display = 'none';
       ged.style.display = 'block';
  };