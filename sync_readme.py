import os
from github import Github
from github.GithubException import UnknownObjectException

def sync_readme(org_name, repo_a_name, repo_b_name, target_subdir):
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("GitHub token must be set")
    
    g = Github(github_token)
    
    try:
        org = g.get_organization(org_name)
        repo_a = org.get_repo(repo_a_name)
        repo_b = org.get_repo(repo_b_name)
        
        try:
            readme_a = repo_a.get_contents("README.md")
        except UnknownObjectException:
            print(f"No README.md found in {repo_a_name}")
            return
        
        target_path = f"{target_subdir}/lunch-and-learn.md"
        
        try:
            existing_readme = repo_b.get_contents(target_path)
            repo_b.update_file(
                path=target_path, 
                message=f"Update README from {repo_a_name}", 
                content=readme_a.decoded_content, 
                sha=existing_readme.sha
            )
            print(f"Updated README in {repo_b_name}/{target_path}")
        except UnknownObjectException:
            repo_b.create_file(
                path=target_path, 
                message=f"Add README from {repo_a_name}", 
                content=readme_a.decoded_content
            )
            print(f"Created README in {repo_b_name}/{target_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these with your specific repository details
sync_readme(
    org_name="nimh-dsst", 
    repo_a_name="lunch-and-learn", 
    repo_b_name="dsst-rtd", 
    target_subdir="docs"
)
