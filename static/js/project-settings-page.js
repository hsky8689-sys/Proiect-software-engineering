const permission_denied = 'You do not have the permission to access this section';
async function loadTaskSection(){

}
async function loadRolesSection(){
    try{
        if(!djangoContext.permissions.can_modify_tasks){
            alert(permission_denied);
    }
    }catch (err){
        alert(err);
    }
}

async function loadProjectStatsSection(){
    try{
        var area = document.getElementsByClassName('project-related-posts').item(0);
        area.innerHTML = '';
        let content =
            `<form>
                <h1>Project data</h1><br>
                <label htmlFor="project-title">Project title</label><input id="project-title" name="project-title" type="text"/><br>
                <label htmlFor="project-description">Project description</label><input id="project-desctiption" name="project-description" type="text"/><br>
                <label for="is-private">Is project private(can be accessed via invite only and is hidden to the search engine)</label><input id="is-private" name="privacy" type="checkbox"/><br>
                <h1>Techstack requirements</h1>`;
                try{  const apiUrl = '/projects/settings/'+djangoContext.project.name+'/api-project-domains';
                  const domain_tags =
                    await fetch(apiUrl, {headers: { 'X-Requested-With': 'XMLHttpRequest' }
                  });
                if (domain_tags.ok){
                    const data = await domain_tags.json();
                    const tags = data.domains;
                    tags.forEach(tag=>{
                        content += `<input id="domain-${tag.domain}" placeholder="${tag.domain}"/> <button type="button">Delete domain</button><br>`;
                    });
                }
                else{
                    content += `Could not load or find the project requirements`;
                }
            }catch (err){
                content += err.message;
            }
                content += `<input type="text" placeholder="Add new techstack requirement for project"/><br><button>Add requirement to project</button>\`;
                <h1>Project tags(domains)</h1>`;
            try{  const apiUrl = '/projects/settings/'+djangoContext.project.name+'/api-project-domains';
                  const domain_tags =
                    await fetch(apiUrl, {headers: { 'X-Requested-With': 'XMLHttpRequest' }
                  });
              if (domain_tags.ok){
                const data = await domain_tags.json();
                const tags = data.domains;
                tags.forEach(tag=>{
                    content += `<p>${tag.domain}</p> <button type="button">Delete domain</button><br>`;
                });
              }
              else{
                content += `Could not load the project domain tags`;
              }
            }catch (err){
                content += err.message;
            }
            content += `<input type="text" placeholder="Add new domain to project"/><br><button>Add domains to project</button>`;
            area.innerHTML=content;
    } catch (err) {
        alert(err);
    }
}