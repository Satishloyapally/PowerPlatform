function filterAttachments() {
  let gallery = PowerAppsGallery;
  let searchText = document.getElementById("searchInput").value.toLowerCase();
  gallery.Items = gallery.Items.filter(item => item.name.toLowerCase().includes(searchText));
}

document.getElementById("searchButton").addEventListener("click", filterAttachments);

