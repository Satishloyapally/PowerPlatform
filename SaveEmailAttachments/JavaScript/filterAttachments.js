function filterAttachments() {
  let gallery = PowerAppsGallery;
  let searchText = document.getElementById("searchInput").value.toLowerCase();
  gallery.Items = gallery.Items.filter(item => item.name.toLowerCase().includes(searchText));
}

document.getElementById("searchButton").addEventListener("click", filterAttachments);

//Explanation:

//Purpose: Enhance the Power Apps interface to filter attachments based on user input.
//Function: filterAttachments()
//Steps:
//Get the gallery control from Power Apps.
//Get the search input value and convert it to lowercase.
//Filter the gallery items based on the search input.
//Add an event listener to the search button to trigger the filtering function.
