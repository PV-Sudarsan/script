function post(e) {
  e.preventDefault();
  if (!t.value.trim()) return;
  let d = document.createElement('div');
  d.className = 'post';
  d.innerHTML = `<p></p>
    <i class="fa-regular fa-thumbs-up" onclick="['fa-regular','fa-solid','liked'].map(c=>this.classList.toggle(c))"></i>
    <i class="fa-solid fa-share-nodes" onclick="alert('Post shared!')"></i>
    <i class="fa-regular fa-comment" onclick="let c=this.nextElementSibling;c.hidden=!c.hidden"></i>
    <div hidden><input placeholder="Write a comment..."><i class="fa-solid fa-circle-plus" onclick="addC(this)"></i></div>`;
  d.querySelector('p').textContent = t.value;
  feed.prepend(d);
  t.value = '';
}

function addC(b) {
  let i = b.previousElementSibling;
  if (!i.value.trim()) return;
  let p = document.createElement('p');
  p.textContent = i.value;
  b.parentNode.append(p);
  i.value = '';
}
