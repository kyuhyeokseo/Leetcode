<h2><a href="https://leetcode.com/problems/print-binary-tree/?envType=problem-list-v2&envId=24ma7sot">655. Print Binary Tree</a></h2><h3>Medium</h3><hr><p>Given the <code>root</code> of a binary tree, construct a <strong>0-indexed</strong> <code>m x n</code> string matrix <code>res</code> that represents a <strong>formatted layout</strong> of the tree. The formatted layout matrix should be constructed using the following rules:</p>

<ul>
	<li>The <strong>height</strong> of the tree is <code>height</code>&nbsp;and the number of rows <code>m</code> should be equal to <code>height + 1</code>.</li>
	<li>The number of columns <code>n</code> should be equal to <code>2<sup>height+1</sup> - 1</code>.</li>
	<li>Place the <strong>root node</strong> in the <strong>middle</strong> of the <strong>top row</strong> (more formally, at location <code>res[0][(n-1)/2]</code>).</li>
	<li>For each node that has been placed in the matrix at position <code>res[r][c]</code>, place its <strong>left child</strong> at <code>res[r+1][c-2<sup>height-r-1</sup>]</code> and its <strong>right child</strong> at <code>res[r+1][c+2<sup>height-r-1</sup>]</code>.</li>
	<li>Continue this process until all the nodes in the tree have been placed.</li>
	<li>Any empty cells should contain the empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>Return <em>the constructed matrix </em><code>res</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg" style="width: 141px; height: 181px;" />
<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 
[[&quot;&quot;,&quot;1&quot;,&quot;&quot;],
&nbsp;[&quot;2&quot;,&quot;&quot;,&quot;&quot;]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg" style="width: 207px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> 
[[&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;1&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;],
&nbsp;[&quot;&quot;,&quot;2&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;3&quot;,&quot;&quot;],
&nbsp;[&quot;&quot;,&quot;&quot;,&quot;4&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2<sup>10</sup>]</code>.</li>
	<li><code>-99 &lt;= Node.val &lt;= 99</code></li>
	<li>The depth of the tree will be in the range <code>[1, 10]</code>.</li>
</ul>
