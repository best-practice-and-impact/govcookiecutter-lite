# Govcookiecutter-lite Prompts

We have opted to create a slimmed down install which comes with the bare minimum.
Hence we have reduced the number of questions prompted to the user.
Although these may be self explanatory by name, this table has been created to outline what each prompt represents and how it should be used.

<style>
.table-custom {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
}
.table-custom th, .table-custom td {
    border: 1px solid #ddd;
    padding: 8px;
}
.table-custom th {
    /* background-color: #f2f2f2; */
    text-align: left;
}
</style>

<table class="table-custom">
    <thead>
        <tr>
            <th>Prompt Name</th>
            <th>Description</th>
            <th>Example Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>project_name</code></td>
            <td>The name to assign to your new project.<br>Underscores are advised against unless they increase readability</td>
            <td><code>your_new_project_name</code></td>
        </tr>
        <tr>
            <td><code>organisation_handle</code></td>
            <td>The short identifier for your organisation or team.<br>Used in project TOML to identify authors of the package.</td>
            <td><code>ONS</code></td>
        </tr>
    </tbody>
</table>
