const cssModulesPlugin = require('esbuild-css-modules-plugin')

require('esbuild')
  .build({
    entryPoints: ['./src/index.js'],
    outdir: 'public',
    sourcemap: true,
    bundle: true,
    format: 'esm',
    target: ['es2020'],
    loader: {
      '.js': 'jsx',
    },
    plugins: [cssModulesPlugin],
  })
  .catch(() => process.exit(1))
