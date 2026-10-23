const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../web/tv.js'), 'utf8');

function launch(id, native, fails) {
  const opened = [];
  let result;
  const context = {
    window: { tizen: { application: {
      getCurrentApplication: () => ({ appInfo: { id: 'FreeMyTVio.FreeMyTV' } }),
      getAppInfo: app => {
        assert.equal(app, 'org.tizen.netflix-app');
        if (!native) throw new Error('NotFoundError');
        return { id: app };
      },
      launch: (app, ok, error) => { opened.push(app); (fails ? error : ok)(); }
    } } },
    setTimeout
  };
  vm.createContext(context);
  vm.runInContext(source, context);
  context.TV.launch(id, null, ok => { result = ok; });
  return { opened, result };
}

assert.deepEqual(launch('RN1MCdNq8t.Netflix', true), {
  opened: ['org.tizen.netflix-app'], result: true
});
assert.deepEqual(launch('RN1MCdNq8t.Netflix', false), {
  opened: ['RN1MCdNq8t.Netflix'], result: true
});
assert.deepEqual(launch('org.tizen.netflix-app', true), {
  opened: ['org.tizen.netflix-app'], result: true
});
assert.deepEqual(launch('YouTube.app', true), { opened: ['YouTube.app'], result: true });
assert.deepEqual(launch('RN1MCdNq8t.Netflix', true, true), {
  opened: ['org.tizen.netflix-app'], result: false
});
console.log('Samsung Netflix: 5 cenários passaram.');
