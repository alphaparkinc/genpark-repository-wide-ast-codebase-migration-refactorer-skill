from client import RepositoryWideAstCodebaseMigrationRefactorerClient

def main():
    client = RepositoryWideAstCodebaseMigrationRefactorerClient()
    res = client.execute_fleet_migration("Migrate React 18 class components to React 19 hooks", "src/**/*.tsx")
    print(f"Status: {res['migration_status']}")
    print(f"Files Modified: {res['files_modified_count']}")
    print(f"AST Transforms: {res['ast_transforms_applied']}")

if __name__ == "__main__":
    main()
