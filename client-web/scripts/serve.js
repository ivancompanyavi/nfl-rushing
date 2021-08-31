const cssModulesPlugin = require('esbuild-css-modules-plugin')

require('esbuild')
  .build({
    entryPoints: ['./src/index.js'],
    outfile: 'public/out.js',
    sourcemap: true,
    bundle: true,
    loader: {
      '.js': 'jsx',
    },
    plugins: [cssModulesPlugin()],
    watch: true,
  })
  .catch(() => process.exit(1))
