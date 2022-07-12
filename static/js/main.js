//get search form and page link
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// form exists
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++ ){
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()
      

      //get data
      let page = this.dataset.page
      
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

      searchForm.submit()
    })
  }
}
