const cssModulesPlugin = require('esbuild-css-modules-plugin')

require('esbuild')
  .serve(
    {
      servedir: 'public',
      port: 8000,
    },
    {
      entryPoints: ['./src/index.js'],
      outfile: 'public/out.js',
      sourcemap: true,
      bundle: true,
      loader: {
        '.js': 'jsx',
      },
      plugins: [cssModulesPlugin()],
    }
  )
  .catch(() => process.exit(1))
