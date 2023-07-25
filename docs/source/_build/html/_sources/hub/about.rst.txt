=======================
About the Teaching Hub
=======================
Welcome to the third iteration of the DWR Teaching Hub. In Summer 2021, we decided it was time to migrate the Teaching Hub away from the WordPress platform where it has lived for the last several years. Since the Teaching Hub primarily serves text that is often changing and because of the robust cloud storage options provided by the University, the complexity and vulnerability of a database-centric CMS for the Teaching Hub is no longer warranted. 

The Teaching Hub's new platform is a Python-based documentation generator engine called `Sphinx <https://www.sphinx-doc.org/en/master/>`_ hosted through a service called `ReadTheDocs <https://readthedocs.org/>`_. The primary advantage to this approach is that the Teaching Hub no longer has any significant security vulnerabilities because there is no database. Static, versioned documentation is also a best practice for professional technical communicators.  

Editing the Teaching Hub
------------------------
.. sidebar:: GitHub edits

    .. figure:: /assets/ghedit.png 

    To edit any Teaching Hub page on GitHub, click the pencil to open the text editor. 

Anyone can submit edits to the DWR Teaching Hub. If you notice a typo, an error, or outdated information anywhere on the Teaching Hub, you can correct it by clicking **Edit on GitHub** in the top right of the page. You'll need to log in to GitHub to submit edits. You can sign in with any Microsoft account or create a brand new account by clicking "Sign Up" in the top right. 

Once you're logged in to GitHub, click the pencil icon to edit the page. 

ReStructured Text
~~~~~~~~~~~~~~~~~~
All Teaching Hub pages are written in a markup language called ReStructured Text. ReST is similar to Markdown in that it allows you to design complex documents with multiple formats using only plain text. Once you get the hang of it, it's just as fast as writing a document in Word or Google Docs and you don't have to worry about how it will be displayed on the web.

.. Admonition:: More Information

    * `Read about the ReST markup language used by Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
    * `ReStructured Text/Sphinx Cheat Sheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_


Fixing typos or errors in content doesn't require the use of ReST markup. Just looking at the raw version of a page in the GitHub editor should show you everything you need to know. 

Submitting an Edit
~~~~~~~~~~~~~~~~~~~
.. figure:: /assets/ghpullreq.png 

Enter a title and a brief description of your page edits and subnit a Pull Request. 

When you are done making edits to a page, write a title and description of the changes you made and click **Propose Changes**. This creates a `GitHub Pull Request <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_ on the Teaching Hub main repository. We'll review the edits and, if accepted, we'll merge them into the production version of the Teaching Hub. 

Don't worry about messing something up. Pull Requests have to be approved before they alter production pages. If you make a mistake in your Pull Request, we'll either ask you to fix or or fix it ourselves before merging it into the live Teaching Hub. 

Questions? Contact `Andrew Davis <mailto:addavis@olemiss.edu>`_.