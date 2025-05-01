<h2><a href="https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal">Longest Common Prefix After at Most One Removal</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given two strings <code>s</code> and <code>t</code>.</p>

<p>Return the <strong>length</strong> of the <strong>longest common <span data-keyword="string-prefix">prefix</span></strong> between <code>s</code> and <code>t</code> after removing <strong>at most</strong> one character from <code>s</code>.</p>

<p><strong>Note:</strong> <code>s</code> can be left without any removal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;madxa&quot;, t = &quot;madam&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing <code>s[3]</code> from <code>s</code> results in <code>&quot;mada&quot;</code>, which has a longest common prefix of length 4 with <code>t</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;, t = &quot;eetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing <code>s[0]</code> from <code>s</code> results in <code>&quot;eetcode&quot;</code>, which matches <code>t</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;one&quot;, t = &quot;one&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>No removal is needed.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a&quot;, t = &quot;b&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> and <code>t</code> cannot have a common prefix.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> contain only lowercase English letters.</li>
</ul>
